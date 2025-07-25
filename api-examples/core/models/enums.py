from enum import StrEnum

class CaseInsensitiveStrEnum(StrEnum):
    @classmethod
    def _missing_(cls, name):
        for member in cls:
            if member.name.lower() == name.lower():
                return member
            
class Platform(CaseInsensitiveStrEnum):
    FILECOIN = 'filecoin'
    BITGO = 'bitgo'
    BINANCE = 'binance'
    POLYGON = 'polygon'
    AVAX = 'avax'
    OPTIMISM = 'optimism'
    CELO = 'celo'
    BITCOIN = 'bitcoin'
    SOLANA = 'solana'
    CARDANO = 'cardano'
    AKASH = 'akash'
    BAND = 'band'
    EMONEY = 'emoney'
    SECRET = 'secret'
    SENTINEL = 'sentinel'
    KAVA = 'kava'
    PERSISTENCE = 'persistence'
    OSMOSIS = 'osmosis'
    PROVENANCE = 'provenance'
    INJECTIVE = 'injective'
    JUNO = 'juno'
    GRAVITY = 'gravity'
    CHIHUAHUA = 'chihuahua'
    STARGAZE = 'stargaze'
    COMDEX = 'comdex'
    UMEE = 'umee'
    AXELAR = 'axelar'
    EVMOS = 'evmos'
    IRISNET = 'irisnet'
    CRESCENT = 'crescent'
    TGRADE = 'tgrade'
    BINANCE_EXCHANGE = 'binance_exchange'
    BINANCE_EXCHANGE_TR = 'binance_exchange_tr'
    COINBASE_PRIME = 'coinbase_prime'
    COINBASE = 'coinbase'
    ETHEREUM = 'ethereum'
    ARBITRUM = 'arbitrum'
    FANTOM = 'fantom'
    KRAKEN = 'kraken'
    FLARE_SONGBIRD = 'flare_songbird'
    MINA = 'mina'
    POLKADOT = 'polkadot'
    KUSAMA = 'kusama'
    ETHEREUM2 = 'ethereum2'
    COSMOS = 'cosmos'
    AURORA = 'aurora'
    RONIN = 'ronin'
    GNOSIS_CHAIN = 'gnosis_chain'
    KUCOIN = 'kucoin'
    KLAYTN = 'klaytn'
    FALCONX = 'falconx'
    ALGORAND = 'algorand'
    GEMINI = "gemini"
    FTX = 'ftx'
    FTXUS = 'ftxus'
    MOONBEAM = 'moonbeam'
    ACALA = 'acala'
    COINBASE_COMMERCE = 'coinbase_commerce'
    COINBASE_EXCHANGE = 'coinbase_exchange'
    AGORIC = 'agoric'
    CASPER = 'casper'
    OASIS = 'oasis'
    SOMMELIER = 'sommelier'
    HARMONY = 'harmony'
    NEAR = 'near'
    NYM = 'nym'
    ASSET_MANTLE = 'asset_mantle'
    BITCANNA = 'bitcanna'
    # CERBERUS = 'cerberus'
    CRYPTOCOM = 'cryptocom'
    DESMOS = 'desmos'
    KICHAIN = 'kichain'
    LUM = 'lum'
    OMNIFLIX = 'omniflix'
    REGEN = 'regen'
    SIFCHAIN = 'sifchain'
    LIKECOIN = 'likecoin'
    SHENTU = 'shentu'
    AVALANCHE_P_CHAIN = 'avalanche_p_chain'
    AVALANCHE_X_CHAIN = 'avalanche_x_chain'
    BNB = 'bnb'
    FETCHAI = 'fetchai'
    STRIDE = 'stride'
    TERRA2 = 'terra2'
    TERRA = 'terra'
    SKALE = 'skale'
    METIS = 'metis'
    FUSE = 'fuse'
    STACKS = 'stacks'
    RADIX = 'radix'
    BITFINEX = 'bitfinex'
    ASTAR = 'astar'
    STARKNET = 'starknet'
    MIXNET = 'mixnet'
    PAXFUL = 'paxful'
    ASTAR_EVM = 'astar_evm'
    APTOS = 'aptos'
    LUKKA = 'lukka'
    MANUAL = 'manual'
    IMMUTABLEX = 'immutablex'
    FLOW = 'flow'
    SHIDEN = 'shiden'
    SHIDEN_EVM = 'shiden_evm'
    KAVA_EVM = 'kava_evm'
    SUI = 'sui'
    BTCTURK = 'btcturk'
    ASCENDEX = 'ascendex'
    DYDX = 'dydx'
    CELESTIA = 'celestia'
    BITTENSOR = 'bittensor'

class BalanceState(CaseInsensitiveStrEnum):
    LOCKED = 'locked'
    CLAIMABLE = 'claimable'
    LIQUID = 'liquid'
    WALLET = 'wallet'
    VIRTUAL = 'virtual'
    CLAIMED = 'claimed'
    WITHDRAWN = 'withdrawn'
    UNDER_DELEGATION = 'delegated_to_account'
    FAILED = 'failed'
    DEPOSITED = 'deposited'

class PositionType(CaseInsensitiveStrEnum):
    STAKING = 'staking',
    DELEGATED_TO_ACCOUNT = 'delegated_to_account',
    LP = 'lp',
    LENDING = 'lending',
    BORROWING = 'borrowing',
    VESTING = 'vesting'