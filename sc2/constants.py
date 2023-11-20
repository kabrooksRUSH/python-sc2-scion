from collections import defaultdict
from typing import Any, Dict, Set

from sc2.data import Alliance, Attribute, CloakState, DisplayType, TargetType
from sc2.ids.ability_id import AbilityId
from sc2.ids.buff_id import BuffId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.ids.upgrade_id import UpgradeId

mineral_ids: Set[int] = {
    UnitTypeId.RICHMINERALFIELD.value,
    UnitTypeId.RICHMINERALFIELD750.value,
    UnitTypeId.MINERALFIELD.value,
    UnitTypeId.MINERALFIELD450.value,
    UnitTypeId.MINERALFIELD750.value,
    UnitTypeId.LABMINERALFIELD.value,
    UnitTypeId.LABMINERALFIELD750.value,
    UnitTypeId.PURIFIERRICHMINERALFIELD.value,
    UnitTypeId.PURIFIERRICHMINERALFIELD750.value,
    UnitTypeId.PURIFIERMINERALFIELD.value,
    UnitTypeId.PURIFIERMINERALFIELD750.value,
    UnitTypeId.BATTLESTATIONMINERALFIELD.value,
    UnitTypeId.BATTLESTATIONMINERALFIELD750.value,
    UnitTypeId.MINERALFIELDOPAQUE.value,
    UnitTypeId.MINERALFIELDOPAQUE900.value,
}
geyser_ids: Set[int] = {
    UnitTypeId.VESPENEGEYSER.value,
    UnitTypeId.SPACEPLATFORMGEYSER.value,
    UnitTypeId.RICHVESPENEGEYSER.value,
    UnitTypeId.PROTOSSVESPENEGEYSER.value,
    UnitTypeId.PURIFIERVESPENEGEYSER.value,
    UnitTypeId.SHAKURASVESPENEGEYSER.value,
}
transforming: Dict[UnitTypeId, AbilityId] = {
    # Terran structures
    UnitTypeId.BARRACKS: AbilityId.LAND_BARRACKS,
    UnitTypeId.BARRACKSFLYING: AbilityId.LAND_BARRACKS,
    UnitTypeId.COMMANDCENTER: AbilityId.LAND_COMMANDCENTER,
    UnitTypeId.COMMANDCENTERFLYING: AbilityId.LAND_COMMANDCENTER,
    UnitTypeId.ORBITALCOMMAND: AbilityId.LAND_ORBITALCOMMAND,
    UnitTypeId.ORBITALCOMMANDFLYING: AbilityId.LAND_ORBITALCOMMAND,
    UnitTypeId.FACTORY: AbilityId.LAND_FACTORY,
    UnitTypeId.FACTORYFLYING: AbilityId.LAND_FACTORY,
    UnitTypeId.STARPORT: AbilityId.LAND_STARPORT,
    UnitTypeId.STARPORTFLYING: AbilityId.LAND_STARPORT,
    UnitTypeId.SUPPLYDEPOT: AbilityId.MORPH_SUPPLYDEPOT_RAISE,
    UnitTypeId.SUPPLYDEPOTLOWERED: AbilityId.MORPH_SUPPLYDEPOT_LOWER,
    # Terran units
    UnitTypeId.HELLION: AbilityId.MORPH_HELLION,
    UnitTypeId.HELLIONTANK: AbilityId.MORPH_HELLBAT,
    UnitTypeId.LIBERATOR: AbilityId.MORPH_LIBERATORAAMODE,
    UnitTypeId.LIBERATORAG: AbilityId.MORPH_LIBERATORAGMODE,
    UnitTypeId.SIEGETANK: AbilityId.UNSIEGE_UNSIEGE,
    UnitTypeId.SIEGETANKSIEGED: AbilityId.SIEGEMODE_SIEGEMODE,
    UnitTypeId.THOR: AbilityId.MORPH_THOREXPLOSIVEMODE,
    UnitTypeId.THORAP: AbilityId.MORPH_THORHIGHIMPACTMODE,
    UnitTypeId.VIKINGASSAULT: AbilityId.MORPH_VIKINGASSAULTMODE,
    UnitTypeId.VIKINGFIGHTER: AbilityId.MORPH_VIKINGFIGHTERMODE,
    UnitTypeId.WIDOWMINE: AbilityId.BURROWUP,
    UnitTypeId.WIDOWMINEBURROWED: AbilityId.BURROWDOWN,
    # Protoss structures
    UnitTypeId.GATEWAY: AbilityId.MORPH_GATEWAY,
    UnitTypeId.WARPGATE: AbilityId.MORPH_WARPGATE,
    # Protoss units
    UnitTypeId.OBSERVER: AbilityId.MORPH_OBSERVERMODE,
    UnitTypeId.OBSERVERSIEGEMODE: AbilityId.MORPH_SURVEILLANCEMODE,
    UnitTypeId.WARPPRISM: AbilityId.MORPH_WARPPRISMTRANSPORTMODE,
    UnitTypeId.WARPPRISMPHASING: AbilityId.MORPH_WARPPRISMPHASINGMODE,
    # Zerg structures
    UnitTypeId.SPINECRAWLER: AbilityId.SPINECRAWLERROOT_SPINECRAWLERROOT,
    UnitTypeId.SPINECRAWLERUPROOTED: AbilityId.SPINECRAWLERUPROOT_SPINECRAWLERUPROOT,
    UnitTypeId.SPORECRAWLER: AbilityId.SPORECRAWLERROOT_SPORECRAWLERROOT,
    UnitTypeId.SPORECRAWLERUPROOTED: AbilityId.SPORECRAWLERUPROOT_SPORECRAWLERUPROOT,
    # Zerg units
    UnitTypeId.BANELING: AbilityId.BURROWUP_BANELING,
    UnitTypeId.BANELINGBURROWED: AbilityId.BURROWDOWN_BANELING,
    UnitTypeId.DRONE: AbilityId.BURROWUP_DRONE,
    UnitTypeId.DRONEBURROWED: AbilityId.BURROWDOWN_DRONE,
    UnitTypeId.HYDRALISK: AbilityId.BURROWUP_HYDRALISK,
    UnitTypeId.HYDRALISKBURROWED: AbilityId.BURROWDOWN_HYDRALISK,
    UnitTypeId.INFESTOR: AbilityId.BURROWUP_INFESTOR,
    UnitTypeId.INFESTORBURROWED: AbilityId.BURROWDOWN_INFESTOR,
    UnitTypeId.INFESTORTERRAN: AbilityId.BURROWUP_INFESTORTERRAN,
    UnitTypeId.INFESTORTERRANBURROWED: AbilityId.BURROWDOWN_INFESTORTERRAN,
    UnitTypeId.LURKERMP: AbilityId.BURROWUP_LURKER,
    UnitTypeId.LURKERMPBURROWED: AbilityId.BURROWDOWN_LURKER,
    UnitTypeId.OVERSEER: AbilityId.MORPH_OVERSEERMODE,
    UnitTypeId.OVERSEERSIEGEMODE: AbilityId.MORPH_OVERSIGHTMODE,
    UnitTypeId.QUEEN: AbilityId.BURROWUP_QUEEN,
    UnitTypeId.QUEENBURROWED: AbilityId.BURROWDOWN_QUEEN,
    UnitTypeId.ROACH: AbilityId.BURROWUP_ROACH,
    UnitTypeId.ROACHBURROWED: AbilityId.BURROWDOWN_ROACH,
    UnitTypeId.SWARMHOSTBURROWEDMP: AbilityId.BURROWDOWN_SWARMHOST,
    UnitTypeId.SWARMHOSTMP: AbilityId.BURROWUP_SWARMHOST,
    UnitTypeId.ULTRALISK: AbilityId.BURROWUP_ULTRALISK,
    UnitTypeId.ULTRALISKBURROWED: AbilityId.BURROWDOWN_ULTRALISK,
    UnitTypeId.ZERGLING: AbilityId.BURROWUP_ZERGLING,
    UnitTypeId.ZERGLINGBURROWED: AbilityId.BURROWDOWN_ZERGLING,
    # Xayid structures
    # I dont think there are any
    # Xayid units
    UnitTypeId.MASSALISK: AbilityId.BIOMASSCAVERNRESEARCH_MUTATEHUNKER,
    UnitTypeId.MASSALISKHUNKERED: AbilityId.HUNKER_HUNKEREDFORM,
    #TODO: This one below is wrong, i cant find correct one for some reason
    UnitTypeId.MENDLING: AbilityId.MENDLINGSACRIFICIALMUTATION_MUTATEINTOSACRIFICIALMUTATION,
    # Genetron structures
    UnitTypeId.REPULSOR: AbilityId.REPULSORUNBURROW_STATICDUNBURROW,
    UnitTypeId.REPULSORBURROWED: AbilityId.REPULSORBURROW_STATICDBURROW,
    UnitTypeId.INTERDICTOR: AbilityId.INTERDICTORUNBURROW_STATICDUNBURROW,
    UnitTypeId.INTERDICTORBURROWED: AbilityId.INTERDICTORBURROW_STATICDBURROW,
    # Genetron units
    UnitTypeId.SCION_PROCESSOR: AbilityId.PROCESSORSTATICMODEOFF_PROCESSORCANCELSTATICMODE,
    UnitTypeId.SCION_PROCESSORSTATIC: AbilityId.PROCESSORSTATICMODE_PROCESSORSTATICMODE,
    UnitTypeId.MOLE: AbilityId.MOLEDEACTIVATE_MOBILIZECANNON,
    UnitTypeId.MOLEROOTED: AbilityId.MOLEACTIVATE_DEPLOYCANNON,
    #TODO: The mole rooted can be created by mole unburrow also and mole can be created from unroot in burrow mode, figure out how to handle this...
    UnitTypeId.MOLEBURROWED: AbilityId.MOLEBURY_MOLECONCEAL,
    # Keiron structures
    UnitTypeId.CITADELCHARGED: AbilityId.CITADELCHARGEMORPH_CHARGECITADEL,
    # Keiron units
    UnitTypeId.ECHO: AbilityId.ECHOFIGHTERMODE_FIGHTERMODEECHO,
    UnitTypeId.ECHODM: AbilityId.ECHODISCORDMODE_DISCORDMODE,
}
# For now only contains units that cost supply, used in bot_ai.do()
abilityid_to_unittypeid: Dict[AbilityId, UnitTypeId] = {
    # Protoss
    AbilityId.NEXUSTRAIN_PROBE: UnitTypeId.PROBE,
    AbilityId.GATEWAYTRAIN_ZEALOT: UnitTypeId.ZEALOT,
    AbilityId.WARPGATETRAIN_ZEALOT: UnitTypeId.ZEALOT,
    AbilityId.TRAIN_ADEPT: UnitTypeId.ADEPT,
    AbilityId.TRAINWARP_ADEPT: UnitTypeId.ADEPT,
    AbilityId.GATEWAYTRAIN_STALKER: UnitTypeId.STALKER,
    AbilityId.WARPGATETRAIN_STALKER: UnitTypeId.STALKER,
    AbilityId.GATEWAYTRAIN_SENTRY: UnitTypeId.SENTRY,
    AbilityId.WARPGATETRAIN_SENTRY: UnitTypeId.SENTRY,
    AbilityId.GATEWAYTRAIN_DARKTEMPLAR: UnitTypeId.DARKTEMPLAR,
    AbilityId.WARPGATETRAIN_DARKTEMPLAR: UnitTypeId.DARKTEMPLAR,
    AbilityId.GATEWAYTRAIN_HIGHTEMPLAR: UnitTypeId.HIGHTEMPLAR,
    AbilityId.WARPGATETRAIN_HIGHTEMPLAR: UnitTypeId.HIGHTEMPLAR,
    AbilityId.ROBOTICSFACILITYTRAIN_OBSERVER: UnitTypeId.OBSERVER,
    AbilityId.ROBOTICSFACILITYTRAIN_COLOSSUS: UnitTypeId.COLOSSUS,
    AbilityId.ROBOTICSFACILITYTRAIN_IMMORTAL: UnitTypeId.IMMORTAL,
    AbilityId.ROBOTICSFACILITYTRAIN_WARPPRISM: UnitTypeId.WARPPRISM,
    AbilityId.STARGATETRAIN_CARRIER: UnitTypeId.CARRIER,
    AbilityId.STARGATETRAIN_ORACLE: UnitTypeId.ORACLE,
    AbilityId.STARGATETRAIN_PHOENIX: UnitTypeId.PHOENIX,
    AbilityId.STARGATETRAIN_TEMPEST: UnitTypeId.TEMPEST,
    AbilityId.STARGATETRAIN_VOIDRAY: UnitTypeId.VOIDRAY,
    AbilityId.NEXUSTRAINMOTHERSHIP_MOTHERSHIP: UnitTypeId.MOTHERSHIP,
    # Terran
    AbilityId.COMMANDCENTERTRAIN_SCV: UnitTypeId.SCV,
    AbilityId.BARRACKSTRAIN_MARINE: UnitTypeId.MARINE,
    AbilityId.BARRACKSTRAIN_GHOST: UnitTypeId.GHOST,
    AbilityId.BARRACKSTRAIN_MARAUDER: UnitTypeId.MARAUDER,
    AbilityId.BARRACKSTRAIN_REAPER: UnitTypeId.REAPER,
    AbilityId.FACTORYTRAIN_HELLION: UnitTypeId.HELLION,
    AbilityId.FACTORYTRAIN_SIEGETANK: UnitTypeId.SIEGETANK,
    AbilityId.FACTORYTRAIN_THOR: UnitTypeId.THOR,
    AbilityId.FACTORYTRAIN_WIDOWMINE: UnitTypeId.WIDOWMINE,
    AbilityId.TRAIN_HELLBAT: UnitTypeId.HELLIONTANK,
    AbilityId.TRAIN_CYCLONE: UnitTypeId.CYCLONE,
    AbilityId.STARPORTTRAIN_RAVEN: UnitTypeId.RAVEN,
    AbilityId.STARPORTTRAIN_VIKINGFIGHTER: UnitTypeId.VIKINGFIGHTER,
    AbilityId.STARPORTTRAIN_MEDIVAC: UnitTypeId.MEDIVAC,
    AbilityId.STARPORTTRAIN_BATTLECRUISER: UnitTypeId.BATTLECRUISER,
    AbilityId.STARPORTTRAIN_BANSHEE: UnitTypeId.BANSHEE,
    AbilityId.STARPORTTRAIN_LIBERATOR: UnitTypeId.LIBERATOR,
    # Zerg
    AbilityId.LARVATRAIN_DRONE: UnitTypeId.DRONE,
    AbilityId.LARVATRAIN_OVERLORD: UnitTypeId.OVERLORD,
    AbilityId.LARVATRAIN_ZERGLING: UnitTypeId.ZERGLING,
    AbilityId.LARVATRAIN_ROACH: UnitTypeId.ROACH,
    AbilityId.LARVATRAIN_HYDRALISK: UnitTypeId.HYDRALISK,
    AbilityId.LARVATRAIN_MUTALISK: UnitTypeId.MUTALISK,
    AbilityId.LARVATRAIN_CORRUPTOR: UnitTypeId.CORRUPTOR,
    AbilityId.LARVATRAIN_ULTRALISK: UnitTypeId.ULTRALISK,
    AbilityId.LARVATRAIN_INFESTOR: UnitTypeId.INFESTOR,
    AbilityId.LARVATRAIN_VIPER: UnitTypeId.VIPER,
    AbilityId.LOCUSTTRAIN_SWARMHOST: UnitTypeId.SWARMHOSTMP,
    AbilityId.TRAINQUEEN_QUEEN: UnitTypeId.QUEEN,
    #Xayid
    AbilityId.BIRTHSCAVENGER_BIRTHSCAVENGER: UnitTypeId.SCAVENGER,
    AbilityId.MUTATEXAYIDUNITS_XAYIDLING: UnitTypeId.XAYIDLING,
    AbilityId.MUTATEXAYIDUNITS_ROAMER: UnitTypeId.ROAMER,
    AbilityId.MUTATEXAYIDUNITS_ERODER: UnitTypeId.ERODER,
    AbilityId.MUTATEXAYIDUNITS_SCORPALISK: UnitTypeId.SCORPALISK,
    AbilityId.MUTATEXAYIDUNITS_MENDLING: UnitTypeId.MENDLING,
    AbilityId.MUTATEXAYIDUNITS_CASNOLISK: UnitTypeId.CASNOLISK,
    AbilityId.BIOMASSHATCHERYLARVAMUTATEXAYIDUNITS_REVILER: UnitTypeId.REVILER,
    AbilityId.BIOMASSHATCHERYLARVAMUTATEXAYIDUNITS_FERRION: UnitTypeId.FERRION,
    AbilityId.BIOMASSHATCHERYLARVAMUTATEXAYIDUNITS_MASSALISK: UnitTypeId.MASSALISK,
    AbilityId.BIOMASSHATCHERYLARVAMUTATEXAYIDUNITS_PROWLER: UnitTypeId.PROWLER,
    AbilityId.BIOMASSHATCHERYLARVAMUTATEXAYIDUNITS_SPITTER: UnitTypeId.SPITTER,
    AbilityId.AERIALNESTWASPMUTATEXAYIDFLYERS_RAPTOR: UnitTypeId.RAPTOR,
    AbilityId.AERIALNESTWASPMUTATEXAYIDFLYERS_ASSAILANT: UnitTypeId.ASSAILANT,
    AbilityId.AERIALNESTWASPMUTATEXAYIDFLYERS_EXTERMINATOR: UnitTypeId.EXTERMINATOR,
    AbilityId.AERIALNESTWASPMUTATEXAYIDFLYERS_XAYITHOAN: UnitTypeId.XAYITHOAN,
    AbilityId.AERIALNESTWASPMUTATEXAYIDFLYERS_KRAKEN: UnitTypeId.KRAKEN,
    AbilityId.PLACEACIDNEST_PLACEACIDNEST: UnitTypeId.ACIDNESTBUILD,
    #TODO: This ^ may be wrong, check it later... It may be unittypeid.acidnest
    #Genetron
    AbilityId.PROCESSINGCORETRAIN_ACR: UnitTypeId.ACR,
    AbilityId.TRAINLIGHTWEIGHTMECHS_FABRICATESPITFIRE: UnitTypeId.SPITFIRE,
    AbilityId.TRAINLIGHTWEIGHTMECHS_FABRICATEBLITZER: UnitTypeId.BLITZER,
    AbilityId.TRAINLIGHTWEIGHTMECHS_FABRICATEFIXER: UnitTypeId.FIXER,
    AbilityId.TRAINLIGHTWEIGHTMECHS_FABRICATEAQUILA: UnitTypeId.AQUILA,
    AbilityId.TRAINLIGHTWEIGHTMECHS_FABRICATEEQUALIZER: UnitTypeId.EQUALIZER,
    AbilityId.TRAINHEAVYWEIGHTMECHS_FABRICATEINCITER: UnitTypeId.INCITER,
    AbilityId.TRAINHEAVYWEIGHTMECHS_FABRICATEMOLE: UnitTypeId.MOLE,
    AbilityId.TRAINHEAVYWEIGHTMECHS_FABRICATETESLA: UnitTypeId.TESLA,
    AbilityId.TRAINHEAVYWEIGHTMECHS_FABRICATETORRENT: UnitTypeId.TORRENT,
    AbilityId.TRAINHEAVYWEIGHTMECHS_FABRICATEVIRTUS: UnitTypeId.VIRTUS,
    AbilityId.BUILDAIRCRAFT_FABRICATEAVENGERGENETRON: UnitTypeId.SCION_AVENGER,
    AbilityId.BUILDAIRCRAFT_FABRICATEBADGER: UnitTypeId.BADGER,
    AbilityId.BUILDAIRCRAFT_FABRICATEBOAR: UnitTypeId.BOAR,
    AbilityId.BUILDAIRCRAFT_FABRICATECOURIER: UnitTypeId.COURIER,
    AbilityId.BUILDAIRCRAFT_FABRICATEHORNET: UnitTypeId.HORNET,
    AbilityId.BUILDAIRCRAFT_FABRICATEJUPITER: UnitTypeId.JUPITER,
    AbilityId.LAUNCHSHOCKCHARGE_LAUNCHSHOCKCHARGE: UnitTypeId.CLOAKCHARGE,
    AbilityId.LAUNCHCLOAKCHARGE_LAUNCHCLOAKCHARGE: UnitTypeId.CLOAKCHARGE,
    #Keiron
    AbilityId.KEIRONCITADELTRAIN_CONVERTER: UnitTypeId.CONVERTER,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEPARIAH: UnitTypeId.PARIAH,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEVOLT: UnitTypeId.VOLT,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZESUBJECTER: UnitTypeId.SUBJECTER,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEPULSAR: UnitTypeId.PULSAR,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZECRUX: UnitTypeId.CRUX,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEUMBRA: UnitTypeId.UMBRA,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEWARD: UnitTypeId.WARD,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEMYRIAD: UnitTypeId.MYRIAD,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEINDUCER: UnitTypeId.INDUCER,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZETITAN: UnitTypeId.TITAN,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEFUSE: UnitTypeId.FUSE,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEECHO: UnitTypeId.ECHO,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEAURORA: UnitTypeId.AURORA,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEAPERTURE: UnitTypeId.APERTURE,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEHARBINGER: UnitTypeId.HARBINGER,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEGYRE: UnitTypeId.GYRE,
    AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEPARAGON: UnitTypeId.PARAGON,
    AbilityId.KEIRONCITADELAEGISTRAIN_AEGIS: UnitTypeId.AEGIS
}

IS_STRUCTURE: int = Attribute.Structure.value
IS_LIGHT: int = Attribute.Light.value
IS_ARMORED: int = Attribute.Armored.value
IS_BIOLOGICAL: int = Attribute.Biological.value
IS_MECHANICAL: int = Attribute.Mechanical.value
IS_MASSIVE: int = Attribute.Massive.value
IS_PSIONIC: int = Attribute.Psionic.value
UNIT_BATTLECRUISER: UnitTypeId = UnitTypeId.BATTLECRUISER
UNIT_ORACLE: UnitTypeId = UnitTypeId.ORACLE
TARGET_GROUND: Set[int] = {TargetType.Ground.value, TargetType.Any.value}
TARGET_AIR: Set[int] = {TargetType.Air.value, TargetType.Any.value}
TARGET_BOTH = TARGET_GROUND | TARGET_AIR
IS_SNAPSHOT = DisplayType.Snapshot.value
IS_VISIBLE = DisplayType.Visible.value
IS_PLACEHOLDER = DisplayType.Placeholder.value
IS_MINE = Alliance.Self.value
IS_ENEMY = Alliance.Enemy.value
IS_CLOAKED: Set[int] = {CloakState.Cloaked.value, CloakState.CloakedDetected.value, CloakState.CloakedAllied.value}
IS_REVEALED: int = CloakState.CloakedDetected.value
CAN_BE_ATTACKED: Set[int] = {CloakState.NotCloaked.value, CloakState.CloakedDetected.value}
IS_CARRYING_MINERALS: Set[BuffId] = {BuffId.CARRYMINERALFIELDMINERALS, BuffId.CARRYHIGHYIELDMINERALFIELDMINERALS}
IS_CARRYING_VESPENE: Set[BuffId] = {
    BuffId.CARRYHARVESTABLEVESPENEGEYSERGAS,
    BuffId.CARRYHARVESTABLEVESPENEGEYSERGASPROTOSS,
    BuffId.CARRYHARVESTABLEVESPENEGEYSERGASZERG,
}
IS_CARRYING_RESOURCES: Set[BuffId] = IS_CARRYING_MINERALS | IS_CARRYING_VESPENE
IS_ATTACKING: Set[AbilityId] = {
    AbilityId.ATTACK,
    AbilityId.ATTACK_ATTACK,
    AbilityId.ATTACK_ATTACKTOWARDS,
    AbilityId.ATTACK_ATTACKBARRAGE,
    AbilityId.SCAN_MOVE,
}
IS_PATROLLING: AbilityId = AbilityId.PATROL_PATROL
IS_GATHERING: AbilityId = AbilityId.HARVEST_GATHER
IS_RETURNING: AbilityId = AbilityId.HARVEST_RETURN
IS_COLLECTING: Set[AbilityId] = {IS_GATHERING, IS_RETURNING}
IS_CONSTRUCTING_SCV: Set[AbilityId] = {
    AbilityId.TERRANBUILD_ARMORY,
    AbilityId.TERRANBUILD_BARRACKS,
    AbilityId.TERRANBUILD_BUNKER,
    AbilityId.TERRANBUILD_COMMANDCENTER,
    AbilityId.TERRANBUILD_ENGINEERINGBAY,
    AbilityId.TERRANBUILD_FACTORY,
    AbilityId.TERRANBUILD_FUSIONCORE,
    AbilityId.TERRANBUILD_GHOSTACADEMY,
    AbilityId.TERRANBUILD_MISSILETURRET,
    AbilityId.TERRANBUILD_REFINERY,
    AbilityId.TERRANBUILD_SENSORTOWER,
    AbilityId.TERRANBUILD_STARPORT,
    AbilityId.TERRANBUILD_SUPPLYDEPOT,
}
IS_CONSTRUCTING_SCAVENGER: Set[AbilityId] = {
    AbilityId.FORMSTRUCTURES_SCAVENGERNEST,
    AbilityId.FORMSTRUCTURES_SIPHONER,
    AbilityId.FORMSTRUCTURES_FEEDINGPOOL,
    AbilityId.FORMSTRUCTURES_XAYIDDEN,
    AbilityId.FORMSTRUCTURES_MUTAGENCHAMBER,
    AbilityId.FORMSTRUCTURES_BILEPIT,
    AbilityId.FORMSTRUCTURES_CASNOLISKDEN,
    AbilityId.FORMSTRUCTURES_BIOMASSHATCHERY,
    AbilityId.FORMSTRUCTURES_BIOMASSCAVERN,
    AbilityId.FORMSTRUCTURES_AVIANNEST,
    AbilityId.FORMSTRUCTURES_CATALYSTPIT,
    AbilityId.FORMSTRUCTURES_SUNKENWARREN,
}
IS_CONSTRUCTING_CONVERTER: Set[AbilityId] = {
    AbilityId.KEIRONBUILD_CITADEL,
    AbilityId.KEIRONBUILD_FORMULATOR,
    AbilityId.KEIRONBUILD_EDIFICE,
    AbilityId.KEIRONBUILD_RELIQUARY,
    AbilityId.KEIRONBUILD_SANCTUM,
    AbilityId.KEIRONBUILD_CONDUIT,
    AbilityId.KEIRONBUILD_OCULUS,
    AbilityId.KEIRONBUILD_NULLIFIER,
    AbilityId.KEIRONBUILD_STRATUS,
    AbilityId.KEIRONBUILD_ELYSIUM,
    AbilityId.KEIRONBUILD_ATRIUM,
    AbilityId.KEIRONBUILD_PANTHEON,
    AbilityId.KEIRONBUILD_OUTLET,
    AbilityId.KEIRONBUILD_EMPYREAN,
    AbilityId.KEIRONBUILD_ZENITH,
}
IS_REPAIRING: Set[AbilityId] = {
    AbilityId.EFFECT_REPAIR,
    AbilityId.EFFECT_REPAIR_MULE,
    AbilityId.EFFECT_REPAIR_SCV,
    AbilityId.ACRREPAIR_REPAIR}
IS_DETECTOR: Set[UnitTypeId] = {
    UnitTypeId.OBSERVER,
    UnitTypeId.OBSERVERSIEGEMODE,
    UnitTypeId.RAVEN,
    UnitTypeId.MISSILETURRET,
    UnitTypeId.OVERSEER,
    UnitTypeId.OVERSEERSIEGEMODE,
    UnitTypeId.SPORECRAWLER,
    UnitTypeId.BILEPIT,
    UnitTypeId.FERRION,
    UnitTypeId.SCION_PROCESSOR,
    UnitTypeId.SCION_PROCESSORSTATIC,
    UnitTypeId.OCULUS,
    UnitTypeId.GYRE
}
SPEED_UPGRADE_DICT: Dict[UnitTypeId, UpgradeId] = {
    # Terran
    UnitTypeId.MEDIVAC: UpgradeId.MEDIVACRAPIDDEPLOYMENT,
    UnitTypeId.BANSHEE: UpgradeId.BANSHEESPEED,
    # Protoss
    UnitTypeId.ZEALOT: UpgradeId.CHARGE,
    UnitTypeId.OBSERVER: UpgradeId.OBSERVERGRAVITICBOOSTER,
    UnitTypeId.WARPPRISM: UpgradeId.GRAVITICDRIVE,
    UnitTypeId.VOIDRAY: UpgradeId.VOIDRAYSPEEDUPGRADE,
    # Zerg
    UnitTypeId.OVERLORD: UpgradeId.OVERLORDSPEED,
    UnitTypeId.OVERSEER: UpgradeId.OVERLORDSPEED,
    UnitTypeId.ZERGLING: UpgradeId.ZERGLINGMOVEMENTSPEED,
    UnitTypeId.BANELING: UpgradeId.CENTRIFICALHOOKS,
    UnitTypeId.ROACH: UpgradeId.GLIALRECONSTITUTION,
    UnitTypeId.LURKERMP: UpgradeId.DIGGINGCLAWS,
    # Xayid
    UnitTypeId.XAYIDLING: UpgradeId.DEXTEROUSJOINTS,
    UnitTypeId.SCORPALISK: UpgradeId.SCORPALISKMETABOLICS,
    # Genetron
    UnitTypeId.SPITFIRE: UpgradeId.CALIBRATEDENGINES,
    # Keiron
    UnitTypeId.PARIAH: UpgradeId.MODIFIEDGAIT,
    UnitTypeId.VOLT: UpgradeId.MODIFIEDGAIT,
}
SPEED_INCREASE_DICT: Dict[UnitTypeId, float] = {
    # Terran
    UnitTypeId.MEDIVAC: 1.18,
    UnitTypeId.BANSHEE: 1.3636,
    # Protoss
    UnitTypeId.ZEALOT: 1.5,
    UnitTypeId.OBSERVER: 2,
    UnitTypeId.WARPPRISM: 1.3,
    UnitTypeId.VOIDRAY: 1.328,
    # Zerg
    UnitTypeId.OVERLORD: 2.915,
    UnitTypeId.OVERSEER: 1.8015,
    UnitTypeId.ZERGLING: 1.6,
    UnitTypeId.BANELING: 1.18,
    UnitTypeId.ROACH: 1.3333333333,
    UnitTypeId.LURKERMP: 1.1,
    # Xayid
    UnitTypeId.XAYIDLING: .06,
    UnitTypeId.SCORPALISK: 1.18,
    # Genetron
    UnitTypeId.SPITFIRE: 1.75,
    # Keiron
    UnitTypeId.PARIAH: 1.57,
    UnitTypeId.VOLT: 1.22
}
temp1 = set(SPEED_UPGRADE_DICT)
temp2 = set(SPEED_INCREASE_DICT)
assert temp1 == temp2, f"{temp1.symmetric_difference(temp2)}"
del temp1
del temp2
SPEED_INCREASE_ON_CREEP_DICT: Dict[UnitTypeId, float] = {
    UnitTypeId.QUEEN: 2.67,
    UnitTypeId.ZERGLING: 1.3,
    UnitTypeId.BANELING: 1.3,
    UnitTypeId.ROACH: 1.3,
    UnitTypeId.RAVAGER: 1.3,
    UnitTypeId.HYDRALISK: 1.3,
    UnitTypeId.LURKERMP: 1.3,
    UnitTypeId.ULTRALISK: 1.3,
    UnitTypeId.INFESTOR: 1.3,
    UnitTypeId.INFESTORTERRAN: 1.3,
    UnitTypeId.SWARMHOSTMP: 1.3,
    UnitTypeId.LOCUSTMP: 1.4,
    UnitTypeId.SPINECRAWLER: 2.5,
    UnitTypeId.SPORECRAWLER: 2.5,
}
OFF_CREEP_SPEED_UPGRADE_DICT: Dict[UnitTypeId, UpgradeId] = {
    UnitTypeId.HYDRALISK: UpgradeId.EVOLVEMUSCULARAUGMENTS,
    UnitTypeId.ULTRALISK: UpgradeId.ANABOLICSYNTHESIS,
}
OFF_CREEP_SPEED_INCREASE_DICT: Dict[UnitTypeId, float] = {
    UnitTypeId.HYDRALISK: 1.25,
    UnitTypeId.ULTRALISK: 1.2,
}
temp1 = set(OFF_CREEP_SPEED_UPGRADE_DICT)
temp2 = set(OFF_CREEP_SPEED_INCREASE_DICT)
assert temp1 == temp2, f"{temp1.symmetric_difference(temp2)}"
del temp1
del temp2
# Movement speed gets altered by this factor if it is affected by this buff
SPEED_ALTERING_BUFFS: Dict[BuffId, float] = {
    # Stimpack increases speed by 1.5
    BuffId.STIMPACK: 1.5,
    BuffId.STIMPACKMARAUDER: 1.5,
    BuffId.CHARGEUP: 2.2,  # x2.8 speed up in pre version 4.11
    # Concussive shells of Marauder reduce speed by 50%
    BuffId.DUTCHMARAUDERSLOW: 0.5,
    # Time Warp of Mothership reduces speed by 50%
    BuffId.TIMEWARPPRODUCTION: 0.5,
    # Fungal Growth of Infestor reduces speed by 75%
    BuffId.FUNGALGROWTH: 0.25,
    # Inhibitor Zones reduce speed by 35%
    BuffId.INHIBITORZONETEMPORALFIELD: 0.65,
    # TODO there is a new zone coming (acceleration zone) which increase movement speed, ultralisk will be affected by this

    # TODO: Fill these out later, I'm not sure if they are used for much
    BuffId.OVERCHARGESPEEDBOOST: 1
}
UNIT_PHOTONCANNON: UnitTypeId = UnitTypeId.PHOTONCANNON
UNIT_COLOSSUS: UnitTypeId = UnitTypeId.COLOSSUS
# Used in unit_command.py and action.py to combine only certain abilities
#TODO: Check if we need to do anything with these. (I don't know what they do right now)
COMBINEABLE_ABILITIES: Set[AbilityId] = {
    AbilityId.MOVE,
    AbilityId.ATTACK,
    AbilityId.SCAN_MOVE,
    AbilityId.STOP,
    AbilityId.HOLDPOSITION,
    AbilityId.PATROL,
    AbilityId.HARVEST_GATHER,
    AbilityId.HARVEST_RETURN,
    AbilityId.EFFECT_REPAIR,
    AbilityId.LIFT,
    AbilityId.BURROWDOWN,
    AbilityId.BURROWUP,
    AbilityId.SIEGEMODE_SIEGEMODE,
    AbilityId.UNSIEGE_UNSIEGE,
    AbilityId.MORPH_LIBERATORAAMODE,
    AbilityId.EFFECT_STIM,
    AbilityId.MORPH_UPROOT,
    AbilityId.EFFECT_BLINK,
    AbilityId.MORPH_ARCHON,
}
#TODO: Check if we need to do anything with these fake effects. (I don't know what they do right now)
FakeEffectRadii: Dict[int, float] = {
    UnitTypeId.KD8CHARGE.value: 2,
    UnitTypeId.PARASITICBOMBDUMMY.value: 3,
    UnitTypeId.FORCEFIELD.value: 1.5,
}
FakeEffectID: Dict[int, str] = {
    UnitTypeId.KD8CHARGE.value: "KD8CHARGE",
    UnitTypeId.PARASITICBOMBDUMMY.value: "PARASITICBOMB",
    UnitTypeId.FORCEFIELD.value: "FORCEFIELD",
}

TERRAN_STRUCTURES_REQUIRE_SCV: Set[UnitTypeId] = {
    UnitTypeId.ARMORY,
    UnitTypeId.BARRACKS,
    UnitTypeId.BUNKER,
    UnitTypeId.COMMANDCENTER,
    UnitTypeId.ENGINEERINGBAY,
    UnitTypeId.FACTORY,
    UnitTypeId.FUSIONCORE,
    UnitTypeId.GHOSTACADEMY,
    UnitTypeId.MISSILETURRET,
    UnitTypeId.REFINERY,
    UnitTypeId.REFINERYRICH,
    UnitTypeId.SENSORTOWER,
    UnitTypeId.STARPORT,
    UnitTypeId.SUPPLYDEPOT,
}

XAYID_STRUCTURES_REQUIRE_SCAVENGER: Set[UnitTypeId] = {
    UnitTypeId.SCAVENGERNEST,
    UnitTypeId.SIPHONER,
    UnitTypeId.FEEDINGPOOL,
    UnitTypeId.XAYIDDEN,
    UnitTypeId.MUTAGENCHAMBER,
    UnitTypeId.BILEPIT,
    UnitTypeId.CASNOLISK,
    UnitTypeId.BIOMASSHATCHERY,
    UnitTypeId.BIOMASSCAVERN,
    UnitTypeId.AVIANNEST,
    UnitTypeId.CATALYSTPIT,
    UnitTypeId.SUNKENWARREN
}

KEIRON_STRUCTURES_REQUIRE_CONVERTER: Set[UnitTypeId] = {
    UnitTypeId.CITADEL,
    UnitTypeId.FORMULATOR,
    UnitTypeId.EDIFICE,
    UnitTypeId.RELIQUARY,
    UnitTypeId.SANCTUM,
    UnitTypeId.CONDUIT,
    UnitTypeId.OCULUS,
    UnitTypeId.NULLIFIER,
    UnitTypeId.STRATUS,
    UnitTypeId.ELYSIUM,
    UnitTypeId.FOUNDRY,
    UnitTypeId.ATRIUM,
    UnitTypeId.PANTHEON,
    UnitTypeId.OUTLET,
    UnitTypeId.EMPYREAN,
    UnitTypeId.ZENITH
}

def return_NOTAUNIT() -> UnitTypeId:
    # NOTAUNIT = 0
    return UnitTypeId.NOTAUNIT


# Hotfix for structures and units as the API does not seem to return the correct values, e.g. ghost and thor have None in the requirements
TERRAN_TECH_REQUIREMENT: Dict[UnitTypeId, UnitTypeId] = defaultdict(
    return_NOTAUNIT,
    {
        UnitTypeId.MISSILETURRET: UnitTypeId.ENGINEERINGBAY,
        UnitTypeId.SENSORTOWER: UnitTypeId.ENGINEERINGBAY,
        UnitTypeId.PLANETARYFORTRESS: UnitTypeId.ENGINEERINGBAY,
        UnitTypeId.BARRACKS: UnitTypeId.SUPPLYDEPOT,
        UnitTypeId.ORBITALCOMMAND: UnitTypeId.BARRACKS,
        UnitTypeId.BUNKER: UnitTypeId.BARRACKS,
        UnitTypeId.GHOST: UnitTypeId.GHOSTACADEMY,
        UnitTypeId.GHOSTACADEMY: UnitTypeId.BARRACKS,
        UnitTypeId.FACTORY: UnitTypeId.BARRACKS,
        UnitTypeId.ARMORY: UnitTypeId.FACTORY,
        UnitTypeId.HELLIONTANK: UnitTypeId.ARMORY,
        UnitTypeId.THOR: UnitTypeId.ARMORY,
        UnitTypeId.STARPORT: UnitTypeId.FACTORY,
        UnitTypeId.FUSIONCORE: UnitTypeId.STARPORT,
        UnitTypeId.BATTLECRUISER: UnitTypeId.FUSIONCORE,
    },
)
PROTOSS_TECH_REQUIREMENT: Dict[UnitTypeId, UnitTypeId] = defaultdict(
    return_NOTAUNIT,
    {
        UnitTypeId.PHOTONCANNON: UnitTypeId.FORGE,
        UnitTypeId.CYBERNETICSCORE: UnitTypeId.GATEWAY,
        UnitTypeId.SENTRY: UnitTypeId.CYBERNETICSCORE,
        UnitTypeId.STALKER: UnitTypeId.CYBERNETICSCORE,
        UnitTypeId.ADEPT: UnitTypeId.CYBERNETICSCORE,
        UnitTypeId.TWILIGHTCOUNCIL: UnitTypeId.CYBERNETICSCORE,
        UnitTypeId.SHIELDBATTERY: UnitTypeId.CYBERNETICSCORE,
        UnitTypeId.TEMPLARARCHIVE: UnitTypeId.TWILIGHTCOUNCIL,
        UnitTypeId.DARKSHRINE: UnitTypeId.TWILIGHTCOUNCIL,
        UnitTypeId.HIGHTEMPLAR: UnitTypeId.TEMPLARARCHIVE,
        UnitTypeId.DARKTEMPLAR: UnitTypeId.DARKSHRINE,
        UnitTypeId.STARGATE: UnitTypeId.CYBERNETICSCORE,
        UnitTypeId.TEMPEST: UnitTypeId.FLEETBEACON,
        UnitTypeId.CARRIER: UnitTypeId.FLEETBEACON,
        UnitTypeId.MOTHERSHIP: UnitTypeId.FLEETBEACON,
        UnitTypeId.ROBOTICSFACILITY: UnitTypeId.CYBERNETICSCORE,
        UnitTypeId.ROBOTICSBAY: UnitTypeId.ROBOTICSFACILITY,
        UnitTypeId.COLOSSUS: UnitTypeId.ROBOTICSBAY,
        UnitTypeId.DISRUPTOR: UnitTypeId.ROBOTICSBAY,
    },
)
ZERG_TECH_REQUIREMENT: Dict[UnitTypeId, UnitTypeId] = defaultdict(
    return_NOTAUNIT,
    {
        UnitTypeId.ZERGLING: UnitTypeId.SPAWNINGPOOL,
        UnitTypeId.QUEEN: UnitTypeId.SPAWNINGPOOL,
        UnitTypeId.ROACHWARREN: UnitTypeId.SPAWNINGPOOL,
        UnitTypeId.BANELINGNEST: UnitTypeId.SPAWNINGPOOL,
        UnitTypeId.SPINECRAWLER: UnitTypeId.SPAWNINGPOOL,
        UnitTypeId.SPORECRAWLER: UnitTypeId.SPAWNINGPOOL,
        UnitTypeId.ROACH: UnitTypeId.ROACHWARREN,
        UnitTypeId.BANELING: UnitTypeId.BANELINGNEST,
        UnitTypeId.LAIR: UnitTypeId.SPAWNINGPOOL,
        UnitTypeId.OVERSEER: UnitTypeId.LAIR,
        UnitTypeId.OVERLORDTRANSPORT: UnitTypeId.LAIR,
        UnitTypeId.INFESTATIONPIT: UnitTypeId.LAIR,
        UnitTypeId.INFESTOR: UnitTypeId.INFESTATIONPIT,
        UnitTypeId.SWARMHOSTMP: UnitTypeId.INFESTATIONPIT,
        UnitTypeId.HYDRALISKDEN: UnitTypeId.LAIR,
        UnitTypeId.HYDRALISK: UnitTypeId.HYDRALISKDEN,
        UnitTypeId.LURKERDENMP: UnitTypeId.HYDRALISKDEN,
        UnitTypeId.LURKERMP: UnitTypeId.LURKERDENMP,
        UnitTypeId.SPIRE: UnitTypeId.LAIR,
        UnitTypeId.MUTALISK: UnitTypeId.SPIRE,
        UnitTypeId.CORRUPTOR: UnitTypeId.SPIRE,
        UnitTypeId.NYDUSNETWORK: UnitTypeId.LAIR,
        UnitTypeId.HIVE: UnitTypeId.INFESTATIONPIT,
        UnitTypeId.VIPER: UnitTypeId.HIVE,
        UnitTypeId.ULTRALISKCAVERN: UnitTypeId.HIVE,
        UnitTypeId.GREATERSPIRE: UnitTypeId.HIVE,
        UnitTypeId.BROODLORD: UnitTypeId.GREATERSPIRE,
    },
)

XAYID_TECH_REQUIREMENT: Dict[UnitTypeId, UnitTypeId] = defaultdict(
    return_NOTAUNIT,
    {
        UnitTypeId.XAYIDDEN: UnitTypeId.FEEDINGPOOL,
        UnitTypeId.MUTAGENCHAMBER: UnitTypeId.XAYIDDEN,
        UnitTypeId.BILEPIT: UnitTypeId.XAYIDDEN,
        UnitTypeId.CASNOLISK: UnitTypeId.MUTAGENCHAMBER,
        UnitTypeId.BIOMASSHATCHERY: UnitTypeId.MUTAGENCHAMBER,
        UnitTypeId.BIOMASSCAVERN: UnitTypeId.BIOMASSHATCHERY,
        UnitTypeId.AVIANNEST: UnitTypeId.MUTAGENCHAMBER,
        UnitTypeId.CATALYSTPIT: UnitTypeId.AVIANNEST,
        UnitTypeId.SUNKENWARREN: UnitTypeId.CATALYSTPIT,
        UnitTypeId.SCORPALISK: UnitTypeId.MUTAGENCHAMBER,
        UnitTypeId.MENDLING: UnitTypeId.MUTAGENCHAMBER,
        UnitTypeId.CASNOLISK: UnitTypeId.CASNOLISKDEN,
        UnitTypeId.ROAMER: UnitTypeId.MUTAGENCHAMBER,
        UnitTypeId.ERODER: UnitTypeId.CASNOLISKDEN,
        UnitTypeId.MASSALISK: UnitTypeId.BIOMASSCAVERN,
        UnitTypeId.EXTERMINATOR: UnitTypeId.CATALYSTPIT,
        UnitTypeId.XAYITHOAN: UnitTypeId.CATALYSTPIT,
        UnitTypeId.KRAKEN: UnitTypeId.SUNKENWARREN,
    },
)

GENETRON_TECH_REQUIREMENT: Dict[UnitTypeId, UnitTypeId] = defaultdict(
    return_NOTAUNIT,
    {
        UnitTypeId.NODE: UnitTypeId.PROCESSINGCORE,
        UnitTypeId.MANUFACTURER: UnitTypeId.NODE,
        UnitTypeId.ANALYSISTERMINAL: UnitTypeId.NODE,
        UnitTypeId.RELAYTOWER: UnitTypeId.MANUFACTURER,
        UnitTypeId.REPULSOR: UnitTypeId.ANALYSISTERMINAL,
        UnitTypeId.INTERDICTOR: UnitTypeId.ANALYSISTERMINAL,
        UnitTypeId.FABRICATOR: UnitTypeId.MANUFACTURER,
        UnitTypeId.ASSEMBLYARRAY: UnitTypeId.RELAYTOWER,
        UnitTypeId.GENERATOR: UnitTypeId.RELAYTOWER,
        UnitTypeId.OLYMPUS: UnitTypeId.GENERATOR,
        UnitTypeId.TECHVAULT: UnitTypeId.ANALYSISTERMINAL,
        UnitTypeId.CHEMICALFIRM: UnitTypeId.TECHVAULT,
        UnitTypeId.OUTFITTINGSTATION: UnitTypeId.ANALYSISTERMINAL,
        UnitTypeId.ORDNANCECACHE: UnitTypeId.TECHVAULT,
        UnitTypeId.BLITZER: UnitTypeId.ANALYSISTERMINAL,
        UnitTypeId.FIXER: UnitTypeId.OUTFITTINGSTATION,
        UnitTypeId.EQUALIZER: UnitTypeId.OUTFITTINGSTATION,
        UnitTypeId.AQUILA: UnitTypeId.CHEMICALFIRM,
        UnitTypeId.MOLE: UnitTypeId.ANALYSISTERMINAL,
        UnitTypeId.INCITER: UnitTypeId.TECHVAULT,
        UnitTypeId.TESLA: UnitTypeId.CHEMICALFIRM,
        UnitTypeId.VIRTUS: UnitTypeId.CHEMICALFIRM,
        UnitTypeId.JUPITER: UnitTypeId.ORDNANCECACHE,
        UnitTypeId.BADGER: UnitTypeId.ORDNANCECACHE,
    },
)

KEIRON_TECH_REQUIREMENT: Dict[UnitTypeId, UnitTypeId] = defaultdict(
    return_NOTAUNIT,
    {
        UnitTypeId.EDIFICE: UnitTypeId.CITADEL,
        UnitTypeId.RELIQUARY: UnitTypeId.CITADEL,
        UnitTypeId.SANCTUM: UnitTypeId.EDIFICE,
        UnitTypeId.CONDUIT: UnitTypeId.EDIFICE,
        UnitTypeId.OCULUS: UnitTypeId.EDIFICE,
        UnitTypeId.NULLIFIER: UnitTypeId.RELIQUARY,
        UnitTypeId.STRATUS: UnitTypeId.RELIQUARY,
        UnitTypeId.ELYSIUM: UnitTypeId.SANCTUM,
        UnitTypeId.FOUNDRY: UnitTypeId.SANCTUM,
        UnitTypeId.OUTLET: UnitTypeId.SANCTUM,
        UnitTypeId.ATRIUM: UnitTypeId.FOUNDRY,
        UnitTypeId.PANTHEON: UnitTypeId.ATRIUM,
        UnitTypeId.EMPYREAN: UnitTypeId.SANCTUM,
        UnitTypeId.ZENITH: UnitTypeId.EMPYREAN,
        UnitTypeId.AEGIS: UnitTypeId.PANTHEON,
        #TODO: I don't think units for keiron need to be in here except for aegis but also need to figure out how to implement 'or' requirements for tech tree
    },
)
# Required in 'tech_requirement_progress' bot_ai.py function
EQUIVALENTS_FOR_TECH_PROGRESS: Dict[UnitTypeId, Set[UnitTypeId]] = {
    # Protoss
    UnitTypeId.GATEWAY: {UnitTypeId.WARPGATE},
    UnitTypeId.WARPPRISM: {UnitTypeId.WARPPRISMPHASING},
    UnitTypeId.OBSERVER: {UnitTypeId.OBSERVERSIEGEMODE},
    # Terran
    UnitTypeId.SUPPLYDEPOT: {UnitTypeId.SUPPLYDEPOTLOWERED, UnitTypeId.SUPPLYDEPOTDROP},
    UnitTypeId.BARRACKS: {UnitTypeId.BARRACKSFLYING},
    UnitTypeId.FACTORY: {UnitTypeId.FACTORYFLYING},
    UnitTypeId.STARPORT: {UnitTypeId.STARPORTFLYING},
    UnitTypeId.COMMANDCENTER: {
        UnitTypeId.COMMANDCENTERFLYING,
        UnitTypeId.PLANETARYFORTRESS,
        UnitTypeId.ORBITALCOMMAND,
        UnitTypeId.ORBITALCOMMANDFLYING,
    },
    UnitTypeId.ORBITALCOMMAND: {UnitTypeId.ORBITALCOMMANDFLYING},
    UnitTypeId.HELLION: {UnitTypeId.HELLIONTANK},
    UnitTypeId.WIDOWMINE: {UnitTypeId.WIDOWMINEBURROWED},
    UnitTypeId.SIEGETANK: {UnitTypeId.SIEGETANKSIEGED},
    UnitTypeId.THOR: {UnitTypeId.THORAP},
    UnitTypeId.VIKINGFIGHTER: {UnitTypeId.VIKINGASSAULT},
    UnitTypeId.LIBERATOR: {UnitTypeId.LIBERATORAG},
    # Zerg
    UnitTypeId.LAIR: {UnitTypeId.HIVE},
    UnitTypeId.HATCHERY: {UnitTypeId.LAIR, UnitTypeId.HIVE},
    UnitTypeId.SPIRE: {UnitTypeId.GREATERSPIRE},
    UnitTypeId.SPINECRAWLER: {UnitTypeId.SPINECRAWLERUPROOTED},
    UnitTypeId.SPORECRAWLER: {UnitTypeId.SPORECRAWLERUPROOTED},
    UnitTypeId.OVERLORD: {UnitTypeId.OVERLORDTRANSPORT},
    UnitTypeId.OVERSEER: {UnitTypeId.OVERSEERSIEGEMODE},
    UnitTypeId.DRONE: {UnitTypeId.DRONEBURROWED},
    UnitTypeId.ZERGLING: {UnitTypeId.ZERGLINGBURROWED},
    UnitTypeId.ROACH: {UnitTypeId.ROACHBURROWED},
    UnitTypeId.RAVAGER: {UnitTypeId.RAVAGERBURROWED},
    UnitTypeId.HYDRALISK: {UnitTypeId.HYDRALISKBURROWED},
    UnitTypeId.LURKERMP: {UnitTypeId.LURKERMPBURROWED},
    UnitTypeId.SWARMHOSTMP: {UnitTypeId.SWARMHOSTBURROWEDMP},
    UnitTypeId.INFESTOR: {UnitTypeId.INFESTORBURROWED},
    UnitTypeId.ULTRALISK: {UnitTypeId.ULTRALISKBURROWED},

    # I think the only entry that matters here is citadel and charged citadel. The other equivalencies are leaves in the tech tree
    UnitTypeId.CITADEL: {UnitTypeId.CITADELCHARGED},
    # TODO What about morphing untis? E.g. roach to ravager, overlord to drop-overlord or overseer
}
ALL_GAS: Set[UnitTypeId] = {
    UnitTypeId.ASSIMILATOR,
    UnitTypeId.ASSIMILATORRICH,
    UnitTypeId.REFINERY,
    UnitTypeId.REFINERYRICH,
    UnitTypeId.EXTRACTOR,
    UnitTypeId.EXTRACTORRICH,
    UnitTypeId.SIPHONER,
    UnitTypeId.SIPHONERRICH,
    UnitTypeId.FILTERINGPLANT,
    UnitTypeId.FILTERINGPLANTRICH,
    UnitTypeId.FORMULATOR,
    UnitTypeId.FORMULATORRICH
}
#TODO: Define upgrade bonuses for scion at some point.
DAMAGE_BONUS_PER_UPGRADE: Dict[UnitTypeId, Dict[TargetType, Any]] = {
    #
    # Protoss
    #
    UnitTypeId.PROBE: {
        TargetType.Ground.value: {
            None: 0
        }
    },
    # Gateway Units
    UnitTypeId.ADEPT: {
        TargetType.Ground.value: {
            IS_LIGHT: 1
        }
    },
    UnitTypeId.STALKER: {
        TargetType.Any.value: {
            IS_ARMORED: 1
        }
    },
    UnitTypeId.DARKTEMPLAR: {
        TargetType.Ground.value: {
            None: 5
        }
    },
    UnitTypeId.ARCHON: {
        TargetType.Any.value: {
            None: 3,
            IS_BIOLOGICAL: 1
        }
    },
    # Robo Units
    UnitTypeId.IMMORTAL: {
        TargetType.Ground.value: {
            None: 2,
            IS_ARMORED: 3
        }
    },
    UnitTypeId.COLOSSUS: {
        TargetType.Ground.value: {
            IS_LIGHT: 1
        }
    },
    # Stargate Units
    UnitTypeId.ORACLE: {
        TargetType.Ground.value: {
            None: 0
        }
    },
    UnitTypeId.TEMPEST: {
        TargetType.Ground.value: {
            None: 4
        },
        TargetType.Air.value: {
            None: 3,
            IS_MASSIVE: 2
        }
    },
    #
    # Terran
    #
    UnitTypeId.SCV: {
        TargetType.Ground.value: {
            None: 0
        }
    },
    # Barracks Units
    UnitTypeId.MARAUDER: {
        TargetType.Ground.value: {
            IS_ARMORED: 1
        }
    },
    UnitTypeId.GHOST: {
        TargetType.Any.value: {
            IS_LIGHT: 1
        }
    },
    # Factory Units
    UnitTypeId.HELLION: {
        TargetType.Ground.value: {
            IS_LIGHT: 1
        }
    },
    UnitTypeId.HELLIONTANK: {
        TargetType.Ground.value: {
            None: 2,
            IS_LIGHT: 1
        }
    },
    UnitTypeId.CYCLONE: {
        TargetType.Any.value: {
            None: 2
        }
    },
    UnitTypeId.SIEGETANK: {
        TargetType.Ground.value: {
            None: 2,
            IS_ARMORED: 1
        }
    },
    UnitTypeId.SIEGETANKSIEGED: {
        TargetType.Ground.value: {
            None: 4,
            IS_ARMORED: 1
        }
    },
    UnitTypeId.THOR: {
        TargetType.Ground.value: {
            None: 3
        },
        TargetType.Air.value: {
            IS_LIGHT: 1
        }
    },
    UnitTypeId.THORAP: {
        TargetType.Ground.value: {
            None: 3
        },
        TargetType.Air.value: {
            None: 3,
            IS_MASSIVE: 1
        }
    },
    # Starport Units
    UnitTypeId.VIKINGASSAULT: {
        TargetType.Ground.value: {
            IS_MECHANICAL: 1
        }
    },
    UnitTypeId.LIBERATORAG: {
        TargetType.Ground.value: {
            None: 5
        }
    },
    #
    # Zerg
    #
    UnitTypeId.DRONE: {
        TargetType.Ground.value: {
            None: 0
        }
    },
    # Hatch Tech Units (Queen, Ling, Bane, Roach, Ravager)
    UnitTypeId.BANELING: {
        TargetType.Ground.value: {
            None: 2,
            IS_LIGHT: 2,
            IS_STRUCTURE: 3
        }
    },
    UnitTypeId.ROACH: {
        TargetType.Ground.value: {
            None: 2
        }
    },
    UnitTypeId.RAVAGER: {
        TargetType.Ground.value: {
            None: 2
        }
    },
    # Lair Tech Units (Hydra, Lurker, Ultra)
    UnitTypeId.LURKERMPBURROWED: {
        TargetType.Ground.value: {
            None: 2,
            IS_ARMORED: 1
        }
    },
    UnitTypeId.ULTRALISK: {
        TargetType.Ground.value: {
            None: 3
        }
    },
    # Spire Units (Muta, Corruptor, BL)
    UnitTypeId.CORRUPTOR: {
        TargetType.Air.value: {
            IS_MASSIVE: 1
        }
    },
    UnitTypeId.BROODLORD: {
        TargetType.Ground.value: {
            None: 2
        }
    },
}
TARGET_HELPER = {
    1: "no target",
    2: "Point2",
    3: "Unit",
    4: "Point2 or Unit",
    5: "Point2 or no target",
}
#TODO: Check to see if need to do anything with this (I don't know what it does)
CREATION_ABILITY_FIX: Dict[UnitTypeId, AbilityId] = {
    UnitTypeId.ARCHON: AbilityId.ARCHON_WARP_TARGET,
    UnitTypeId.ASSIMILATORRICH: AbilityId.PROTOSSBUILD_ASSIMILATOR,
    UnitTypeId.BANELINGCOCOON: AbilityId.MORPHZERGLINGTOBANELING_BANELING,
    UnitTypeId.CHANGELING: AbilityId.SPAWNCHANGELING_SPAWNCHANGELING,
    UnitTypeId.EXTRACTORRICH: AbilityId.ZERGBUILD_EXTRACTOR,
    UnitTypeId.INTERCEPTOR: AbilityId.BUILD_INTERCEPTORS,
    UnitTypeId.LURKERMPEGG: AbilityId.MORPH_LURKER,
    UnitTypeId.MULE: AbilityId.CALLDOWNMULE_CALLDOWNMULE,
    UnitTypeId.RAVAGERCOCOON: AbilityId.MORPHTORAVAGER_RAVAGER,
    UnitTypeId.REFINERYRICH: AbilityId.TERRANBUILD_REFINERY,
    UnitTypeId.TECHLAB: AbilityId.BUILD_TECHLAB,
    UnitTypeId.PARIAH: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEPARIAH,
    UnitTypeId.VOLT: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEVOLT,
    UnitTypeId.PULSAR: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEPULSAR,
    UnitTypeId.SUBJECTER: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZESUBJECTER,
    UnitTypeId.CRUX: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZECRUX,
    UnitTypeId.MYRIAD: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEMYRIAD,
    UnitTypeId.INDUCER: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEINDUCER,
    UnitTypeId.TITAN: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZETITAN,
    UnitTypeId.WARD: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEWARD,
    UnitTypeId.UMBRA: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEUMBRA,
    UnitTypeId.AURORA: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEAURORA,
    UnitTypeId.ECHO: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEECHO,
    UnitTypeId.FUSE: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEFUSE,
    UnitTypeId.HARBINGER: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEHARBINGER,
    UnitTypeId.APERTURE: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEAPERTURE,
    UnitTypeId.GYRE: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEGYRE,
    UnitTypeId.PARAGON: AbilityId.KEIRONCITADELMATERIALIZE_MATERIALIZEPARAGON,
}
