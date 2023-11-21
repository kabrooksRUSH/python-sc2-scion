from sc2 import maps
from sc2.unit import Unit
from sc2.player import Bot, Computer
from sc2.main import run_game
from sc2.data import Race, Difficulty
from sc2.bot_ai import BotAI
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId
from sc2.ids.ability_id import AbilityId

class XayidBot(BotAI):
    def __init__(self):
        self.is_droning = True

    async def on_start(self):
        assert(self.workers[0].name == "Scavenger"), "Didnt Get Xayid"
        self.race = Race.Xayid

    async def on_building_construction_complete(self, unit: Unit):
        # if unit.type_id == UnitTypeId.SCAVENGERNEST:
        await self.distribute_workers()

    async def on_step(self, iteration: int):
        if self.townhalls:
            nest = self.townhalls.random

            if self.supply_workers < 55 and nest.is_idle and self.is_droning and self.can_afford(UnitTypeId.SCAVENGER):
                nest.train(UnitTypeId.SCAVENGER)

            if self.supply_workers > 22 * self.structures(UnitTypeId.SCAVENGERNEST).amount and self.can_afford(UnitTypeId.SCAVENGERNEST) and self.already_pending(UnitTypeId.SCAVENGERNEST) == 0:
                await self.expand_now()

            if self.supply_left < 2 and self.can_afford(UnitTypeId.FEEDINGPOOL) and self.already_pending(UnitTypeId.FEEDINGPOOL) == 0:
                await self.build(UnitTypeId.FEEDINGPOOL, near=nest, placement_step=5)

            for nest_ready in self.townhalls.ready:
                if not self.already_pending(UnitTypeId.SIPHONER):
                    vgs = self.vespene_geyser.closer_than(15, nest_ready)
                    for vg in vgs:
                        if not self.can_afford(UnitTypeId.SIPHONER):
                            break
                        worker = self.select_build_worker(vg.position)
                        if worker is None:
                            break
                        if not self.gas_buildings or not self.gas_buildings.closer_than(1, vg):
                            worker.build_gas(vg)
                            # worker.stop(queue=True)

            if self.minerals > 500 and not self.already_pending(UnitTypeId.XAYIDDEN):
                pool = self.structures(UnitTypeId.FEEDINGPOOL).random
                await self.build(UnitTypeId.XAYIDDEN, pool, placement_step=1)

            if self.can_afford(UnitTypeId.XAYIDLING) and self.units(UnitTypeId.WORM).amount > 0:
                worm: Unit = self.units(UnitTypeId.WORM).random
                worm.train(UnitTypeId.XAYIDLING)

            if self.units(UnitTypeId.XAYIDLING).amount > 16 and self.supply_left < 4:
                for unit in self.units(UnitTypeId.XAYIDLING).ready.idle:
                    targets = (self.enemy_units | self.enemy_structures).filter(lambda unit: unit.can_be_attacked)
                    if targets:
                        target = targets.closest_to(unit)
                        unit.attack(target)
                    else:
                        unit.attack(self.enemy_start_locations[0])

            if self.structures(UnitTypeId.XAYIDDEN).amount > 0 and self.can_afford(UnitTypeId.MUTAGENCHAMBER) and not self.already_pending(UnitTypeId.MUTAGENCHAMBER) and self.structures(UnitTypeId.MUTAGENCHAMBER).amount < 1:
                await self.build(UnitTypeId.MUTAGENCHAMBER, near=nest, placement_step=6)

            if self.structures(UnitTypeId.MUTAGENCHAMBER).amount > 0 and self.can_afford(UnitTypeId.CASNOLISKDEN) and not self.already_pending(UnitTypeId.CASNOLISKDEN) and self.structures(UnitTypeId.CASNOLISKDEN).amount < 1:
                await self.build(UnitTypeId.CASNOLISKDEN, near=nest, placement_step=6)

            if (self.structures(UnitTypeId.CASNOLISKDEN).ready and self.can_afford(AbilityId.CASNOLISKDENRESEARCH_MUTATEDEXTEROUSJOINTS)
            and self.already_pending_upgrade(UpgradeId.DEXTEROUSJOINTS) == 0):
                den = self.structures(UnitTypeId.CASNOLISKDEN).ready.first
                den.research(UpgradeId.DEXTEROUSJOINTS)

            if (self.structures(UnitTypeId.CASNOLISKDEN).ready and self.can_afford(AbilityId.CASNOLISKDENRESEARCH_MUTATEOCULARACUITY)
            and self.already_pending_upgrade(UpgradeId.OCULARACUITY) == 0):
                den = self.structures(UnitTypeId.CASNOLISKDEN).ready.first
                den.research(UpgradeId.OCULARACUITY)
        
                
def main():
    run_game(maps.get("Xayid"), [
        Bot(Race.Random, XayidBot()),
        Computer(Race.Protoss, Difficulty.Hard)
        # Computer(Race.Terran, Difficulty.Harder)
    ], realtime=False)

if __name__ == "__main__":
    main()