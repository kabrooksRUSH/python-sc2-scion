from sc2 import maps
from sc2.player import Bot, Computer
from sc2.main import run_game
from sc2.data import Race, Difficulty
from sc2.bot_ai import BotAI

class WorkerRushBot(BotAI):
    async def on_start(self):
        await self.client.debug_food()
        await self.client.debug_fast_build()


    async def on_step(self, iteration: int):
        if self.minerals < 10_000:
            await self.client.debug_all_resources()
        elif self.vespene < 10_000:
            await self.client.debug_all_resources()


        # I dont care what the bot does for data collection...
        # if iteration == 0:
        #     for worker in self.workers:
        #         worker.attack(self.enemy_start_locations[0])

run_game(maps.get("allscion"), [
    Bot(Race.Zerg, WorkerRushBot()),
    Computer(Race.Protoss, Difficulty.Medium)
], realtime=True)