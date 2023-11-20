from sc2 import maps
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2.main import run_game
from sc2.data import Race, Difficulty
from sc2.bot_ai import BotAI
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.ability_id import AbilityId

class WorkerRushBot(BotAI):
    def __init__(self):
        self.is_droning = True

    async def on_start(self):
        assert(self.workers[0].name == "Converter"), "Didnt Get Keiron"
        self.race = Race.Keiron

    async def on_building_construction_complete(self, unit: Unit):
        await self.distribute_workers()

    async def on_step(self, iteration: int):

        if self.townhalls:
            citadel = self.townhalls.random

            if self.supply_workers < 80 and citadel.is_idle and self.is_droning:
                if self.can_afford(UnitTypeId.CONVERTER):
                    citadel.train(UnitTypeId.CONVERTER)

            if self.supply_workers == 14 and self.already_pending(UnitTypeId.EDIFICE) == 0 and self.can_afford(UnitTypeId.EDIFICE):
                await self.build(UnitTypeId.EDIFICE, near=citadel, placement_step=6)

            if self.supply_workers == 17 and self.is_droning:
                self.is_droning = False

            if self.supply_workers == 18 and self.already_pending(UnitTypeId.CITADEL) == 0 and self.can_afford(UnitTypeId.CITADEL):
                await self.expand_now()
                self.is_droning = True

            if self.supply_workers == 19 and self.already_pending(UnitTypeId.SANCTUM) == 0 and self.can_afford(UnitTypeId.SANCTUM):
                await self.build(UnitTypeId.SANCTUM, near=citadel, placement_step=6)

            if self.supply_workers == 19 and self.already_pending(UnitTypeId.FORMULATOR) == 0 and self.can_afford(UnitTypeId.FORMULATOR):
                await self.build(UnitTypeId.FORMULATOR, near=citadel)

            if self.supply_workers > 24:
                pos = citadel.position.to2.random_on_distance(3)
                placement = await self.find_placement(AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEVOLT, pos, placement_step=1)
                citadel.materialize(UnitTypeId.VOLT, placement)

        # if iteration == 0:
        #     for worker in self.workers:
        #         worker.attack(self.enemy_start_locations[0])

            # await self.client.debug_create_unit([[UnitTypeId.SPITFIRE, 5, self.game_info.map_center, 1]])



def main():

    run_game(maps.get("Keiron"), [
        Bot(Race.Random, WorkerRushBot()),
        Computer(Race.Random, Difficulty.Medium)
    ], realtime=True)

if __name__ == "__main__":
    main()