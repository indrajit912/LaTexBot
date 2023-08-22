# A class for styling the terminal.
#
# Author: Indrajit Ghosh
#
# Date: Dec 13, 2021
#

class IndraStyle:

    """
    Class that provides various styles (based on ANSI escape codes)
    to the terminal.

    Author: Indrajit Ghosh
    Date: Dec 16, 2021
    
        USAGES:
        1.
            >>> import IndraStyle
            >>> print(f"{IndraStyle.BLINK + IndraStyle.CRIMSON}Hello World!{IndraStyle.END}")

        2.
            To change the 'background' color use the following:
            >>> print(f"{IndraStyle.BG_RED + Hello World!{IndraStyle.END}")

        CAUTION:
            If you are using 'windows' make sure to include the following lines
            at the top of your code:

                # The following things make ANSI works on different platforms too!
                 PLATFORMS = {
                     "linux": ['linux'],
                     "windows": ['win32', 'cygwin', 'msys'],
                     "mac": ['darwin']
                }

                import sys
                if sys.platform in PLATFORMS['windows']: # To make ANSI work on windows system
                    import os
                    os.system("color")
                ##########  xxx  ##########

    """
    

    # Stylings
    BOLD = '\033[1m'
    DIM = '\033[2m' # May be implemented as a light font weight like bold.
    ITALLIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    BLINK_RAPIDLY = '\033[6m' # Not widely supported. 
    INVERT = '\033[7m' # Swap foreground and background colors; inconsistent emulation
    HIDE = '\033[8m' # Not widely supported.
    STRIKE = '\033[9m'
    DEFAULT = '\033[10m'
    DOUBLY_UNDERLINE = '\033[21m'
    OVERLINE = '\033[53m'
    SUPERSCRIPT = '\033[73m'
    SUBSCRIPT = '\033[74m'

    TURN_OFF_ITALLIC = '\033[23m'
    TURN_OFF_UNDERLINE = '\033[24m'
    TURN_OFF_BLINKING = '\033[25m'
    TURN_OFF_INVERT = '\033[27m'
    TURN_OFF_STRIKE = '\033[29m'
    TURN_OFF_OVERLINE = '\033[55m'

    REVEAL = '\033[28m'

    END = '\033[0m'


    # Greek Letters Unicodes
    ALPHA = '\u03B1'
    BETA = '\u03B2'
    GAMMA = '\u03B3'
    DELTA = '\u03B4'
    EPSILON = '\u03B5'
    ZETA = '\u03B6'
    ETA = '\u03B7'
    THETA = '\u03B8'
    IOTA = '\u03B9'
    KAPPA = '\u03BA'
    LAMBDA = '\u03BB'
    MU = '\u03BC'
    NU = '\u03BD'
    XI = '\u03BE'
    OMICRON = '\u03BF'
    PI = '\u03C0'
    PHO = '\u03C1'
    SIGMA = '\u03C3'
    TAU = '\u03C4'
    UPSILON = '\u03C5'
    PHI = '\u03C6'
    CHI = '\u03C7'
    PSI = '\u03C8'
    OMEGA = '\u03C9'

    CAPITAL_GAMMA = '\u0393'
    CAPITAL_DELTA = '\u0394'
    CAPITAL_THETA = '\u0398'
    CAPITAL_LAMBDA = '\u039B'
    CAPITAL_XI = '\u039E'
    CAPITAL_PI = '\u03A0'
    CAPITAL_SIGMA = '\u03C3'
    CAPITAL_PHI = '\u03A6'
    CAPITAL_PSI = '\u03A8'
    CAPITAL_OMEGA = '\u03A9'


    # Emojies
    GRINNING_FACE = '\U0001F600' # 😀
    GRINNING_FACE_WITH_BIG_EYES = '\U0001F603' # 😃
    GRINNING_FACE_WITH_SMILING_EYES = '\U0001F604' # 😄
    BEAMING_FACE_WITH_SMILING_EYES = '\U0001F601' # 😁
    GRINNING_SQUINTING_FACE = '\U0001F606' # 😆
    THINKING_FACE = '\U0001F914' # 🤔
    EXPRESSION_LESS_FACE = '\U0001F611' # 😑
    FACE_WITH_MEDICAL_MASK = '\U0001F637' # 😷
    KISSING_FACE = '\U0001F617' # 😗
    FACE_WITH_TONGUE = '\U0001F61B' # 😛
    MONEY_MOUTH_FACE = '\U0001F911' # 🤑


    # Foreground Colors
    MAROON = '\x1b[38;2;128;0;0m'
    DARK_RED = '\x1b[38;2;139;0;0m'
    BROWN = '\x1b[38;2;165;42;42m'
    FIREBRICK = '\x1b[38;2;178;34;34m'
    CRIMSON = '\x1b[38;2;220;20;60m'
    RED = '\x1b[38;2;255;0;0m'
    TOMATO = '\x1b[38;2;255;99;71m'
    CORAL = '\x1b[38;2;255;127;80m'
    INDIAN_RED = '\x1b[38;2;205;92;92m'
    LIGHT_CORAL = '\x1b[38;2;240;128;128m'
    DARK_SALMON = '\x1b[38;2;233;150;122m'
    SALMON = '\x1b[38;2;250;128;114m'
    LIGHT_SALMON = '\x1b[38;2;255;160;122m'
    ORANGE_RED = '\x1b[38;2;255;69;0m'
    DARK_ORANGE = '\x1b[38;2;255;140;0m'
    ORANGE = '\x1b[38;2;255;165;0m'
    GOLD = '\x1b[38;2;255;215;0m'
    DARK_GOLDEN_ROD = '\x1b[38;2;184;134;11m'
    GOLDEN_ROD = '\x1b[38;2;218;165;32m'
    PALE_GOLDEN_ROD = '\x1b[38;2;238;232;170m'
    DARK_KHAKI = '\x1b[38;2;189;183;107m'
    KHAKI = '\x1b[38;2;240;230;140m'
    OLIVE = '\x1b[38;2;128;128;0m'
    YELLOW = '\x1b[38;2;255;255;0m'
    YELLOW_GREEN = '\x1b[38;2;154;205;50m'
    DARK_OLIVE_GREEN = '\x1b[38;2;85;107;47m'
    OLIVE_DRAB = '\x1b[38;2;107;142;35m'
    LAWN_GREEN = '\x1b[38;2;124;252;0m'
    CHARTREUSE = '\x1b[38;2;127;255;0m'
    GREEN_YELLOW = '\x1b[38;2;173;255;47m'
    DARK_GREEN = '\x1b[38;2;0;100;0m'
    GREEN = '\x1b[38;2;0;128;0m'
    FOREST_GREEN = '\x1b[38;2;34;139;34m'
    LIME = '\x1b[38;2;0;255;0m'
    LIME_GREEN = '\x1b[38;2;50;205;50m'
    LIGHT_GREEN = '\x1b[38;2;144;238;144m'
    PALE_GREEN = '\x1b[38;2;152;251;152m'
    DARK_SEA_GREEN = '\x1b[38;2;143;188;143m'
    MEDIUM_SPRING_GREEN = '\x1b[38;2;0;250;154m'
    SPRING_GREEN = '\x1b[38;2;0;255;127m'
    SEA_GREEN = '\x1b[38;2;46;139;87m'
    MEDIUM_AQUA_MARINE = '\x1b[38;2;102;205;170m'
    MEDIUM_SEA_GREEN = '\x1b[38;2;60;179;113m'
    LIGHT_SEA_GREEN = '\x1b[38;2;32;178;170m'
    DARK_SLATE_GRAY = '\x1b[38;2;47;79;79m'
    TEAL = '\x1b[38;2;0;128;128m'
    DARK_CYAN = '\x1b[38;2;0;139;139m'
    AQUA = '\x1b[38;2;0;255;255m'
    CYAN = '\x1b[38;2;0;255;255m'
    LIGHT_CYAN = '\x1b[38;2;224;255;255m'
    DARK_TURQUOISE = '\x1b[38;2;0;206;209m'
    TURQUOISE = '\x1b[38;2;64;224;208m'
    MEDIUM_TURQUOISE = '\x1b[38;2;72;209;204m'
    PALE_TURQUOISE = '\x1b[38;2;175;238;238m'
    AQUA_MARINE = '\x1b[38;2;127;255;212m'
    POWDER_BLUE = '\x1b[38;2;176;224;230m'
    CADET_BLUE = '\x1b[38;2;95;158;160m'
    STEEL_BLUE = '\x1b[38;2;70;130;180m'
    CORN_FLOWER_BLUE = '\x1b[38;2;100;149;237m'
    DEEP_SKY_BLUE = '\x1b[38;2;0;191;255m'
    DODGER_BLUE = '\x1b[38;2;30;144;255m'
    LIGHT_BLUE = '\x1b[38;2;173;216;230m'
    SKY_BLUE = '\x1b[38;2;135;206;235m'
    LIGHT_SKY_BLUE = '\x1b[38;2;135;206;250m'
    MIDNIGHT_BLUE = '\x1b[38;2;25;25;112m'
    NAVY = '\x1b[38;2;0;0;128m'
    DARK_BLUE = '\x1b[38;2;0;0;139m'
    MEDIUM_BLUE = '\x1b[38;2;0;0;205m'
    BLUE = '\x1b[38;2;0;0;255m'
    ROYAL_BLUE = '\x1b[38;2;65;105;225m'
    BLUE_VIOLET = '\x1b[38;2;138;43;226m'
    INDIGO = '\x1b[38;2;75;0;130m'
    DARK_SLATE_BLUE = '\x1b[38;2;72;61;139m'
    SLATE_BLUE = '\x1b[38;2;106;90;205m'
    MEDIUM_SLATE_BLUE = '\x1b[38;2;123;104;238m'
    MEDIUM_PURPLE = '\x1b[38;2;147;112;219m'
    DARK_MAGENTA = '\x1b[38;2;139;0;139m'
    DARK_VIOLET = '\x1b[38;2;148;0;211m'
    DARK_ORCHID = '\x1b[38;2;153;50;204m'
    MEDIUM_ORCHID = '\x1b[38;2;186;85;211m'
    PURPLE = '\x1b[38;2;128;0;128m'
    THISTLE = '\x1b[38;2;216;191;216m'
    PLUM = '\x1b[38;2;221;160;221m'
    VIOLET = '\x1b[38;2;238;130;238m'
    MAGENTA = '\x1b[38;2;255;0;255m'
    FUCHSIA = '\x1b[38;2;255;0;255m'
    ORCHID = '\x1b[38;2;218;112;214m'
    MEDIUM_VIOLET_RED = '\x1b[38;2;199;21;133m'
    PALE_VIOLET_RED = '\x1b[38;2;219;112;147m'
    DEEP_PINK = '\x1b[38;2;255;20;147m'
    HOT_PINK = '\x1b[38;2;255;105;180m'
    LIGHT_PINK = '\x1b[38;2;255;182;193m'
    PINK = '\x1b[38;2;255;192;203m'
    ANTIQUE_WHITE = '\x1b[38;2;250;235;215m'
    BEIGE = '\x1b[38;2;245;245;220m'
    BISQUE = '\x1b[38;2;255;228;196m'
    BLANCHED_ALMOND = '\x1b[38;2;255;235;205m'
    WHEAT = '\x1b[38;2;245;222;179m'
    CORN_SILK = '\x1b[38;2;255;248;220m'
    LEMON_CHIFFON = '\x1b[38;2;255;250;205m'
    LIGHT_GOLDEN_ROD_YELLOW = '\x1b[38;2;250;250;210m'
    LIGHT_YELLOW = '\x1b[38;2;255;255;224m'
    SADDLE_BROWN = '\x1b[38;2;139;69;19m'
    SIENNA = '\x1b[38;2;160;82;45m'
    CHOCOLATE = '\x1b[38;2;210;105;30m'
    PERU = '\x1b[38;2;205;133;63m'
    SANDY_BROWN = '\x1b[38;2;244;164;96m'
    BURLY_WOOD = '\x1b[38;2;222;184;135m'
    TAN = '\x1b[38;2;210;180;140m'
    ROSY_BROWN = '\x1b[38;2;188;143;143m'
    MOCCASIN = '\x1b[38;2;255;228;181m'
    NAVAJO_WHITE = '\x1b[38;2;255;222;173m'
    PEACH_PUFF = '\x1b[38;2;255;218;185m'
    MISTY_ROSE = '\x1b[38;2;255;228;225m'
    LAVENDER_BLUSH = '\x1b[38;2;255;240;245m'
    LINEN = '\x1b[38;2;250;240;230m'
    OLD_LACE = '\x1b[38;2;253;245;230m'
    PAPAYA_WHIP = '\x1b[38;2;255;239;213m'
    SEA_SHELL = '\x1b[38;2;255;245;238m'
    MINT_CREAM = '\x1b[38;2;245;255;250m'
    SLATE_GRAY = '\x1b[38;2;112;128;144m'
    LIGHT_SLATE_GRAY = '\x1b[38;2;119;136;153m'
    LIGHT_STEEL_BLUE = '\x1b[38;2;176;196;222m'
    LAVENDER = '\x1b[38;2;230;230;250m'
    FLORAL_WHITE = '\x1b[38;2;255;250;240m'
    ALICE_BLUE = '\x1b[38;2;240;248;255m'
    GHOST_WHITE = '\x1b[38;2;248;248;255m'
    HONEYDEW = '\x1b[38;2;240;255;240m'
    IVORY = '\x1b[38;2;255;255;240m'
    AZURE = '\x1b[38;2;240;255;255m'
    SNOW = '\x1b[38;2;255;250;250m'
    BLACK = '\x1b[38;2;0;0;0m'
    DIM_GRAY = '\x1b[38;2;105;105;105m'
    DIM_GREY = '\x1b[38;2;105;105;105m'
    GRAY = '\x1b[38;2;128;128;128m'
    GREY = '\x1b[38;2;128;128;128m'
    DARK_GREY = '\x1b[38;2;169;169;169m'
    DARK_GRAY = '\x1b[38;2;169;169;169m'
    SILVER = '\x1b[38;2;192;192;192m'
    LIGHT_GREY = '\x1b[38;2;211;211;211m'
    LIGHT_GRAY = '\x1b[38;2;211;211;211m'
    GAINSBORO = '\x1b[38;2;220;220;220m'
    WHITE_SMOKE = '\x1b[38;2;245;245;245m'
    WHITE = '\x1b[38;2;255;255;255m'


    # Background Colors
    MAROON_BG = '\x1b[48;2;128;0;0m'
    DARK_RED_BG = '\x1b[48;2;139;0;0m'
    BROWN_BG = '\x1b[48;2;165;42;42m'
    FIREBRICK_BG = '\x1b[48;2;178;34;34m'
    CRIMSON_BG = '\x1b[48;2;220;20;60m'
    RED_BG = '\x1b[48;2;255;0;0m'
    TOMATO_BG = '\x1b[48;2;255;99;71m'
    CORAL_BG = '\x1b[48;2;255;127;80m'
    INDIAN_RED_BG = '\x1b[48;2;205;92;92m'
    LIGHT_CORAL_BG = '\x1b[48;2;240;128;128m'
    DARK_SALMON_BG = '\x1b[48;2;233;150;122m'
    SALMON_BG = '\x1b[48;2;250;128;114m'
    LIGHT_SALMON_BG = '\x1b[48;2;255;160;122m'
    ORANGE_RED_BG = '\x1b[48;2;255;69;0m'
    DARK_ORANGE_BG = '\x1b[48;2;255;140;0m'
    ORANGE_BG = '\x1b[48;2;255;165;0m'
    GOLD_BG = '\x1b[48;2;255;215;0m'
    DARK_GOLDEN_ROD_BG = '\x1b[48;2;184;134;11m'
    GOLDEN_ROD_BG = '\x1b[48;2;218;165;32m'
    PALE_GOLDEN_ROD_BG = '\x1b[48;2;238;232;170m'
    DARK_KHAKI_BG = '\x1b[48;2;189;183;107m'
    KHAKI_BG = '\x1b[48;2;240;230;140m'
    OLIVE_BG = '\x1b[48;2;128;128;0m'
    YELLOW_BG = '\x1b[48;2;255;255;0m'
    YELLOW_GREEN_BG = '\x1b[48;2;154;205;50m'
    DARK_OLIVE_GREEN_BG = '\x1b[48;2;85;107;47m'
    OLIVE_DRAB_BG = '\x1b[48;2;107;142;35m'
    LAWN_GREEN_BG = '\x1b[48;2;124;252;0m'
    CHARTREUSE_BG = '\x1b[48;2;127;255;0m'
    GREEN_YELLOW_BG = '\x1b[48;2;173;255;47m'
    DARK_GREEN_BG = '\x1b[48;2;0;100;0m'
    GREEN_BG = '\x1b[48;2;0;128;0m'
    FOREST_GREEN_BG = '\x1b[48;2;34;139;34m'
    LIME_BG = '\x1b[48;2;0;255;0m'
    LIME_GREEN_BG = '\x1b[48;2;50;205;50m'
    LIGHT_GREEN_BG = '\x1b[48;2;144;238;144m'
    PALE_GREEN_BG = '\x1b[48;2;152;251;152m'
    DARK_SEA_GREEN_BG = '\x1b[48;2;143;188;143m'
    MEDIUM_SPRING_GREEN_BG = '\x1b[48;2;0;250;154m'
    SPRING_GREEN_BG = '\x1b[48;2;0;255;127m'
    SEA_GREEN_BG = '\x1b[48;2;46;139;87m'
    MEDIUM_AQUA_MARINE_BG = '\x1b[48;2;102;205;170m'
    MEDIUM_SEA_GREEN_BG = '\x1b[48;2;60;179;113m'
    LIGHT_SEA_GREEN_BG = '\x1b[48;2;32;178;170m'
    DARK_SLATE_GRAY_BG = '\x1b[48;2;47;79;79m'
    TEAL_BG = '\x1b[48;2;0;128;128m'
    DARK_CYAN_BG = '\x1b[48;2;0;139;139m'
    AQUA_BG = '\x1b[48;2;0;255;255m'
    CYAN_BG = '\x1b[48;2;0;255;255m'
    LIGHT_CYAN_BG = '\x1b[48;2;224;255;255m'
    DARK_TURQUOISE_BG = '\x1b[48;2;0;206;209m'
    TURQUOISE_BG = '\x1b[48;2;64;224;208m'
    MEDIUM_TURQUOISE_BG = '\x1b[48;2;72;209;204m'
    PALE_TURQUOISE_BG = '\x1b[48;2;175;238;238m'
    AQUA_MARINE_BG = '\x1b[48;2;127;255;212m'
    POWDER_BLUE_BG = '\x1b[48;2;176;224;230m'
    CADET_BLUE_BG = '\x1b[48;2;95;158;160m'
    STEEL_BLUE_BG = '\x1b[48;2;70;130;180m'
    CORN_FLOWER_BLUE_BG = '\x1b[48;2;100;149;237m'
    DEEP_SKY_BLUE_BG = '\x1b[48;2;0;191;255m'
    DODGER_BLUE_BG = '\x1b[48;2;30;144;255m'
    LIGHT_BLUE_BG = '\x1b[48;2;173;216;230m'
    SKY_BLUE_BG = '\x1b[48;2;135;206;235m'
    LIGHT_SKY_BLUE_BG = '\x1b[48;2;135;206;250m'
    MIDNIGHT_BLUE_BG = '\x1b[48;2;25;25;112m'
    NAVY_BG = '\x1b[48;2;0;0;128m'
    DARK_BLUE_BG = '\x1b[48;2;0;0;139m'
    MEDIUM_BLUE_BG = '\x1b[48;2;0;0;205m'
    BLUE_BG = '\x1b[48;2;0;0;255m'
    ROYAL_BLUE_BG = '\x1b[48;2;65;105;225m'
    BLUE_VIOLET_BG = '\x1b[48;2;138;43;226m'
    INDIGO_BG = '\x1b[48;2;75;0;130m'
    DARK_SLATE_BLUE_BG = '\x1b[48;2;72;61;139m'
    SLATE_BLUE_BG = '\x1b[48;2;106;90;205m'
    MEDIUM_SLATE_BLUE_BG = '\x1b[48;2;123;104;238m'
    MEDIUM_PURPLE_BG = '\x1b[48;2;147;112;219m'
    DARK_MAGENTA_BG = '\x1b[48;2;139;0;139m'
    DARK_VIOLET_BG = '\x1b[48;2;148;0;211m'
    DARK_ORCHID_BG = '\x1b[48;2;153;50;204m'
    MEDIUM_ORCHID_BG = '\x1b[48;2;186;85;211m'
    PURPLE_BG = '\x1b[48;2;128;0;128m'
    THISTLE_BG = '\x1b[48;2;216;191;216m'
    PLUM_BG = '\x1b[48;2;221;160;221m'
    VIOLET_BG = '\x1b[48;2;238;130;238m'
    MAGENTA_BG = '\x1b[48;2;255;0;255m'
    FUCHSIA_BG = '\x1b[48;2;255;0;255m'
    ORCHID_BG = '\x1b[48;2;218;112;214m'
    MEDIUM_VIOLET_RED_BG = '\x1b[48;2;199;21;133m'
    PALE_VIOLET_RED_BG = '\x1b[48;2;219;112;147m'
    DEEP_PINK_BG = '\x1b[48;2;255;20;147m'
    HOT_PINK_BG = '\x1b[48;2;255;105;180m'
    LIGHT_PINK_BG = '\x1b[48;2;255;182;193m'
    PINK_BG = '\x1b[48;2;255;192;203m'
    ANTIQUE_WHITE_BG = '\x1b[48;2;250;235;215m'
    BEIGE_BG = '\x1b[48;2;245;245;220m'
    BISQUE_BG = '\x1b[48;2;255;228;196m'
    BLANCHED_ALMOND_BG = '\x1b[48;2;255;235;205m'
    WHEAT_BG = '\x1b[48;2;245;222;179m'
    CORN_SILK_BG = '\x1b[48;2;255;248;220m'
    LEMON_CHIFFON_BG = '\x1b[48;2;255;250;205m'
    LIGHT_GOLDEN_ROD_YELLOW_BG = '\x1b[48;2;250;250;210m'
    LIGHT_YELLOW_BG = '\x1b[48;2;255;255;224m'
    SADDLE_BROWN_BG = '\x1b[48;2;139;69;19m'
    SIENNA_BG = '\x1b[48;2;160;82;45m'
    CHOCOLATE_BG = '\x1b[48;2;210;105;30m'
    PERU_BG = '\x1b[48;2;205;133;63m'
    SANDY_BROWN_BG = '\x1b[48;2;244;164;96m'
    BURLY_WOOD_BG = '\x1b[48;2;222;184;135m'
    TAN_BG = '\x1b[48;2;210;180;140m'
    ROSY_BROWN_BG = '\x1b[48;2;188;143;143m'
    MOCCASIN_BG = '\x1b[48;2;255;228;181m'
    NAVAJO_WHITE_BG = '\x1b[48;2;255;222;173m'
    PEACH_PUFF_BG = '\x1b[48;2;255;218;185m'
    MISTY_ROSE_BG = '\x1b[48;2;255;228;225m'
    LAVENDER_BLUSH_BG = '\x1b[48;2;255;240;245m'
    LINEN_BG = '\x1b[48;2;250;240;230m'
    OLD_LACE_BG = '\x1b[48;2;253;245;230m'
    PAPAYA_WHIP_BG = '\x1b[48;2;255;239;213m'
    SEA_SHELL_BG = '\x1b[48;2;255;245;238m'
    MINT_CREAM_BG = '\x1b[48;2;245;255;250m'
    SLATE_GRAY_BG = '\x1b[48;2;112;128;144m'
    LIGHT_SLATE_GRAY_BG = '\x1b[48;2;119;136;153m'
    LIGHT_STEEL_BLUE_BG = '\x1b[48;2;176;196;222m'
    LAVENDER_BG = '\x1b[48;2;230;230;250m'
    FLORAL_WHITE_BG = '\x1b[48;2;255;250;240m'
    ALICE_BLUE_BG = '\x1b[48;2;240;248;255m'
    GHOST_WHITE_BG = '\x1b[48;2;248;248;255m'
    HONEYDEW_BG = '\x1b[48;2;240;255;240m'
    IVORY_BG = '\x1b[48;2;255;255;240m'
    AZURE_BG = '\x1b[48;2;240;255;255m'
    SNOW_BG = '\x1b[48;2;255;250;250m'
    BLACK_BG = '\x1b[48;2;0;0;0m'
    DIM_GRAY_BG = '\x1b[48;2;105;105;105m'
    DIM_GREY_BG = '\x1b[48;2;105;105;105m'
    GRAY_BG = '\x1b[48;2;128;128;128m'
    GREY_BG = '\x1b[48;2;128;128;128m'
    DARK_GREY_BG = '\x1b[48;2;169;169;169m'
    DARK_GRAY_BG = '\x1b[48;2;169;169;169m'
    SILVER_BG = '\x1b[48;2;192;192;192m'
    LIGHT_GREY_BG = '\x1b[48;2;211;211;211m'
    LIGHT_GRAY_BG = '\x1b[48;2;211;211;211m'
    GAINSBORO_BG = '\x1b[48;2;220;220;220m'
    WHITE_SMOKE_BG = '\x1b[48;2;245;245;245m'
    WHITE_BG = '\x1b[48;2;255;255;255m'


def show_quotes():
    
    print(f"\n\n    {IndraStyle.BLINK + IndraStyle.CRIMSON}Hello World!{IndraStyle.END}\n")

    quote1 = f"""
    {IndraStyle.ITALLIC}{IndraStyle.PINK}Pure mathematics{IndraStyle.END} is the world’s best game. 
    It is more absorbing than chess, more of a gamble than poker, and lasts 
    longer than Monopoly. It’s free. It can be played anywhere — {IndraStyle.MEDIUM_VIOLET_RED}Archimedes{IndraStyle.END} 
    did it in a bathtub.
                                            — {IndraStyle.BOLD}Richard J. Trudeau{IndraStyle.END}, mathematician
    """
    print(quote1)

    quote2 = f"""
    {IndraStyle.POWDER_BLUE}Mathematics{IndraStyle.END} consists of proving the {IndraStyle.ORCHID_BG}most{IndraStyle.END} obvious thing in the {IndraStyle.UNDERLINE}least{IndraStyle.END} obvious way.
    
                                            — {IndraStyle.BOLD}George Pólya{IndraStyle.END}, Hungarian mathematician
    """
    print(quote2)

    quote3 = f"""
    {IndraStyle.ITALLIC + IndraStyle.WHEAT}Five{IndraStyle.END} out of {IndraStyle.ITALLIC + IndraStyle.HOT_PINK}four{IndraStyle.END} people have trouble with fractions.
                                            — {IndraStyle.BOLD}Steven Wright{IndraStyle.END}, American stand-up comedian
    """
    print(quote3)

    quote4 = f"""
    Just because we {IndraStyle.YELLOW_GREEN}can’t find{IndraStyle.END} a solution, it doesn’t mean there {IndraStyle.MOCCASIN}isn’t one{IndraStyle.END}.
                                            — {IndraStyle.BOLD}Andrew Wiles{IndraStyle.END}, English mathematician

    """
    print(quote4)


if __name__ == '__main__':

    # The following things make ANSI works on different platforms too!
    PLATFORMS = {
        "linux": ['linux'],
        "windows": ['win32', 'cygwin', 'msys'],
        "mac": ['darwin']
    }

    import sys
    if sys.platform in PLATFORMS['windows']: # To make ANSI work on windows system
        import os
        os.system("color")
    ##########  xxx  ##########
    
    show_quotes()