# coding=utf-8
from otree.api import (
    BaseConstants, )


class Constants(BaseConstants):

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 DESIGN SETUP                                                  #
    #                                                                                                               #
    # ============================================================================================================= #

    # NUMBER OF PLAYERS =========================================================================== #
    #   Please specify how many players per market will participate.                                #
    players_per_group = 4

    # VALUATION VECTORS =========================================================================== #
    #   Different player types can have different valuation vectors for resources. Set the          #
    #   valuation vectors for each type and resource (Please keep in mind that the number of value  #
    #   vectors has to be a number that is completely divisible by the variable                     #
    #   "players_per_group"). E.g., if the market has three types and six resources, set the first  #
    #   six values within the list for a type to a number. Please stick to the scheme below.        #
    #   This app supports up to 10 types and 10 resources. Types are generated by id_in_group.      #
    #   This means that if you have 4 players and 2 types, players 1 and 2 are Type1, and           #
    #   players 3 and 4 are Type2.                                                                  #
    val13_t1 = [18, 13, 8, 3]
    val13_t2 = [13, 18, 8, 3]
    val13_t3 = [3, 18, 8, 13]
    val13_t4 = [8, 13, 3, 18]
    #   Set vectors for multiple types in the following way:
    #       val13_t2 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
    #       val13_t3 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
    #       val13_t4 = [85, 2, 2, 80, 50, 80, 80, 30, 80, 80]
    #       ...

    # prio13 OF RESOURCES OVER PARTICIPANTS =================================================== #
    #   Since this app models only the proposing side as active players, the prio13 of the      #
    #   resources over the players have to be specified. Please assign a priority vector for every  #
    #   resource. The length of each vector has to be equal to the number of players specified      #
    #   above. The structure is [<Player with Priority 1>, <Player with Priority 2>, ...]           #
    prio13_r1 = [1, 4, 2, 3]
    prio13_r2 = [2, 4, 1, 3]
    prio13_r3 = [3, 4, 2, 1]
    prio13_r4 = [4, 2, 1, 3]

    #   Set vectors for multiple resources in the following way:
    #       prio13_r2 = [1, 2]
    #       prio13_r3 = [1, 2]
    #       ...

    # RESOURCE CAPACITIES ========================================================================= #
    #   Set the quota of players that each resource can carry. Fill in as many number as in the     #
    #   valuation vectors.                                                                          #
    capacities = [1, 1, 1, 1]

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 APPEARANCE SETTINGS                                           #
    #                                                                                                               #
    # ============================================================================================================= #

    # FRAMING ===================================================================================== #
    #   Here you can choose between a neutral framing (participants/resources) and a application    #
    #   framing (participants/schools).                                                             #
    application_framing = True

    # SHOW INSTRUCTIONS =========================================================================== #
    #   Should the instructions for the mechanism be included?                                      #
    instructions = False

    # SHOW EXAMPLE IN INSTRUCTIONS ================================================================ #
    #   If "instructions = True", should the instructions also include a minimal example of the     #
    #   mechanism in place?                                                                         #
    instructions_example = False

    # SHOW CONFIRM BUTTON ========================================================================= #
    #   If "confirm_button" is set to "True", players will have to confirm their inputs made on     #
    #   Decision.html to. This can be used to avoid accidental submission of the page.              #
    confirm_button = False

    # SHOW RESULTS ================================================================================ #
    #   Should a results screen be included? The results screen shows a summary of results of the   #
    #   market (i.e., preferences submitted, bids made, clearing bids, allotted resources), and the #
    #   final payoff for the player.                                                                #
    results = True

    # ============================================================================================================= #
    #                                                                                                               #
    #                                                 INFORMATION SETTINGS                                          #
    #                                                                                                               #
    # ============================================================================================================= #

    # SHOW CAPACITIES ============================================================================= #
    #   If set to "True", the quota specified in "capacities" above will be shown to players on the #
    #   decision screen and in the instructions.                                                    #
    show_capacities = False

    # SHOW TYPES ================================================================================== #
    #   If "show_types" is set to "True", players will have a hint on the decision page and in the  #
    #   instructions that there are different types of players in the market. Only works if         #
    #   multiple type vectors have been specified above.                                            #
    show_types = True

    # SHOW OTHERS' val13 ===================================================================== #
    #   Should players see the other players' valuation profiles and on the decision page? Only     #
    #   works if "show_types" has been set to "True" above.                                         #
    show_val13 = True

    # SHOW RESOURCES' prio13 ================================================================== #
    #   Should a player see the resources' prio13 for her in the instructions and on the        #
    #   decision page?                                                                              #
    show_prio13 = False

    ####################################################################################################################
    ####################################################################################################################
    # ------------------------------              DO NOT MODIFY BELOW HERE              ------------------------------ #
    ####################################################################################################################
    ####################################################################################################################

    capacities = [i for i in capacities if i is not None]
    nr_courses = len(capacities)

    val13_list = ["val13_t" + str(i) for i in range(1, 11)]
    val13_raw = []
    for i in val13_list:
        if i in locals():
            val13_raw.append(locals()[i])

    val13 = []
    for i in val13_raw:
        val13.append([j for j in i if j is not None])

    prio13_list = ["prio13_r" + str(i) for i in range(1, 11)]
    prio13_raw = []
    for i in prio13_list:
        if i in locals():
            prio13_raw.append(locals()[i])

    prio13 = []
    for i in prio13_raw:
        prio13.append([j for j in i if j is not None])

    nr_types = len(val13)

    name_in_url = "SHda13"
    num_rounds = 1
