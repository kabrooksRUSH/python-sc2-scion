from sc2 import maps
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2.main import run_game
from sc2.data import Race, Difficulty
from sc2.bot_ai import BotAI
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId
from sc2.ids.ability_id import AbilityId

class GenetronBot(BotAI):
    def __init__(self):
        self.is_droning = True

    async def on_start(self):
        assert(self.workers[0].name == "ACR"), "Didnt Get Genetron"
        self.race = Race.Genetron

    async def on_building_construction_complete(self, unit: Unit):
        # if unit.type_id == UnitTypeId.SCAVENGERNEST:
        await self.distribute_workers()

    async def on_step(self, iteration: int):
        if self.townhalls:
            core = self.townhalls.random

            if core.energy >= 100:
                core(AbilityId.MININGPRIORITY_MININGPRIORITY)

            if self.supply_workers < 55 and core.is_idle and self.is_droning and self.can_afford(UnitTypeId.ACR):
                core.train(UnitTypeId.ACR)

            if self.supply_workers > 22 * self.structures(UnitTypeId.PROCESSINGCORE).amount and self.can_afford(UnitTypeId.PROCESSINGCORE) and self.already_pending(UnitTypeId.PROCESSINGCORE) == 0:
                await self.expand_now()

            if self.supply_left < 3 and self.can_afford(UnitTypeId.NODE) and self.already_pending(UnitTypeId.NODE) == 0:
                await self.build(UnitTypeId.NODE, near=core, placement_step=6)

            for core_ready in self.townhalls.ready:
                if not self.already_pending(UnitTypeId.FILTERINGPLANT):
                    vgs = self.vespene_geyser.closer_than(15, core_ready)
                    for vg in vgs:
                        if not self.can_afford(UnitTypeId.FILTERINGPLANT):
                            break
                        worker = self.select_build_worker(vg.position)
                        if worker is None:
                            break
                        if not self.gas_buildings or not self.gas_buildings.closer_than(1, vg):
                            worker.build_gas(vg)
                            worker.stop(queue=True)

            if self.minerals > 500 and self.already_pending(UnitTypeId.MANUFACTURER) < 3:
                node = self.structures(UnitTypeId.NODE).random
                await self.build(UnitTypeId.MANUFACTURER, node, placement_step=1)

            if self.can_afford(UnitTypeId.SPITFIRE) and self.structures(UnitTypeId.MANUFACTURER).amount > 0:
                man: Unit = self.structures(UnitTypeId.MANUFACTURER).random
                if man.is_idle:
                    man.train(UnitTypeId.SPITFIRE)

            if self.units(UnitTypeId.SPITFIRE).amount > 10 and self.supply_left < 4:
                for unit in self.units(UnitTypeId.SPITFIRE).ready.idle:
                    targets = (self.enemy_units | self.enemy_structures).filter(lambda unit: unit.can_be_attacked)
                    if targets:
                        target = targets.closest_to(unit)
                        unit.attack(target)
                    else:
                        unit.attack(self.enemy_start_locations[0])

            if self.structures(UnitTypeId.MANUFACTURER).amount > 0 and self.can_afford(UnitTypeId.ANALYSISTERMINAL) and not self.already_pending(UnitTypeId.ANALYSISTERMINAL) and self.structures(UnitTypeId.ANALYSISTERMINAL).amount < 1:
                await self.build(UnitTypeId.ANALYSISTERMINAL, near=core, placement_step=6)

            if self.structures(UnitTypeId.ANALYSISTERMINAL).amount > 0 and self.can_afford(UnitTypeId.OUTFITTINGSTATION) and not self.already_pending(UnitTypeId.OUTFITTINGSTATION) and self.structures(UnitTypeId.OUTFITTINGSTATION).amount < 1:
                await self.build(UnitTypeId.OUTFITTINGSTATION, near=core, placement_step=6)

            if (self.structures(UnitTypeId.OUTFITTINGSTATION).ready and self.can_afford(AbilityId.OUTFITTINGSTATIONRESEARCH_RESEARCHSPITFIRECALIBRATEDENGINES)
            and self.already_pending_upgrade(UpgradeId.CALIBRATEDENGINES) == 0):
                den = self.structures(UnitTypeId.OUTFITTINGSTATION).ready.first
                den.research(UpgradeId.CALIBRATEDENGINES)

            if (self.structures(UnitTypeId.OUTFITTINGSTATION).ready and self.can_afford(AbilityId.OUTFITTINGSTATIONRESEARCH_RESEARCHSPITFIREMADCAPROUNDS)
            and self.already_pending_upgrade(UpgradeId.SPITFIREMADCAPROUNDS) == 0):
                den = self.structures(UnitTypeId.OUTFITTINGSTATION).ready.first
                den.research(UpgradeId.SPITFIREMADCAPROUNDS)
        
                
def main():
    run_game(maps.get("Genetron"), [
        Bot(Race.Random, GenetronBot()),
        Computer(Race.Zerg, Difficulty.Hard)
        # Computer(Race.Terran, Difficulty.Harder)
    ], realtime=False)
    # ], realtime=False, save_replay_as="GenetronBotvsHardAI.SC2Replay")

if __name__ == "__main__":
    main()