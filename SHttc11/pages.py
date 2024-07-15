#from otree.api import Currency as c, currency_range
#from ._builtin import Page, WaitPage
#from .models import Constants
from itertools import chain
from .user_settings import Constants
from otree.api import *

# METHOD: =================================================================================== #
# DEFINE VARIABLES USED IN ALL TEMPLATES ==================================================== #
# =========================================================================================== #
print(f"val11 SHttc11: {Constants.val11}")
print(f"prio11 SHttc11: {Constants.prio11}")


def vars_for_all_templates(self):
    return {
        'nr_courses': Constants.nr_courses,
        'players_per_group': Constants.players_per_group,
        'indices': [j for j in range(1, Constants.nr_courses + 1)],
        'val11': self.participant.vars['val11'],
        'val11_others': zip(self.participant.vars['other_types_names'],
                                 self.participant.vars['val11_others']),
        'prio11': self.participant.vars['prio11'],
        'capacities': Constants.capacities
    }


class Instructions(Page):
    pass


class InstructionsFramed(Page):
    pass


class Decision(Page):

    form_model = 'player'

    # METHOD: =================================================================================== #
    # RETRIEVE FORM FIELDS FROM MODELS.PY ======================================================= #
    # =========================================================================================== #
    def get_form_fields(self):
        form_fields = \
            list(chain.from_iterable([list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][1:]))

        return form_fields

    # METHOD: =================================================================================== #
    # CREATE VARIABLES TO DISPLAY ON DECISION.HTML ============================================== #
    # =========================================================================================== #
    def vars_for_template(self):
        form_fields = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][1]

        return {
                'form_fields': form_fields,
                'nr_courses': Constants.nr_courses,
                'indices': [j for j in range(1, Constants.nr_courses + 1)],
                'val11': self.participant.vars['val11'],
                'val11_others': zip(self.participant.vars['other_types_names'],
                                     self.participant.vars['val11_others']),
                'players_per_group': Constants.players_per_group,
                'prio11': self.participant.vars['prio11'],
                'capacities': Constants.capacities,
                'player.role': self.participant.vars['role']
                }

    # METHOD: =================================================================================== #
    # BEFORE NEXT PAGE: WRITE BACK PLAYER PREFS TO PARTICIPANT VARS ============================= #
    # =========================================================================================== #
    def before_next_page(self):
        # CREATE INDICES FOR MOST IMPORTANT VARS ================================================ #
        indices = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][0]
        form_fields = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][1]

        # DYNAMICALLY WRITE BACK PLAYER PREFS TO A LIST OF PREFS ================================ #
        for n, pref in zip(indices, form_fields):
            choice_i = getattr(self.player, pref)
            self.participant.vars['player_prefs'][n - 1] = [int(choice_i)]

    # METHOD: =================================================================================== #
    # CONTROL PREFS: PREFERENCES MUST BE UNIQUE ================================================= #
    # =========================================================================================== #
    '''def error_message(self, values):
        indices = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][0]
        form_fields = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][1]
        sum_of_prefs = sum([values[i] for i in form_fields])

        if sum_of_prefs != sum(indices):
            return 'Ihre Präferenzen müssen von 1 bis %s angegeben werden!' % (indices[-1])'''

    def error_message(self, values):
        indices = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][0]
        form_fields = [list(i) for i in zip(*self.participant.vars['form_fields_plus_index'])][1]
        preferences = [values[i] for i in form_fields]

        # Ensure each index is used exactly once
        if sorted(preferences) != list(range(1, len(indices) + 1)):
            return 'Ihre Präferenzen müssen von 1 bis %s angegeben werden!' % (len(indices))



class ResultsWaitPage(WaitPage):

    # METHOD: =================================================================================== #
    # AFTER ALL PLAYERS HAVE SUBMITTED PREFS: RUN TTC MECHANISM AND SET PLAYERS' PAYOFFS ======== #
    # =========================================================================================== #
    def after_all_players_arrive(self):
        self.group.get_allocation()
        self.group.set_payoffs()


class Results(Page):

    # METHOD: =================================================================================== #
    # CREATE VARIABLES TO DISPLAY ON RESULTS.HTML =============================================== #
    # =========================================================================================== #

    def before_next_page(self):
        # Store the original payoff
        base_payoff = float(self.player.payoff)

        # Calculate half of the payoff, formatted to two decimal places
        half_payoff = base_payoff / 2

        # Calculate the final payoff with show-up fee, formatted to two decimal places
        final_payoff = half_payoff + 6

        # Store the payoff in participant vars to make it accessible in later apps/pages
        self.participant.vars['SHttc11_payoff'] = "{:.0f}".format(base_payoff)
        self.participant.vars['SHttc11_payoff_half'] = "{:.2f}".format(half_payoff)
        self.participant.vars['SHttc11_payoff_final'] = "{:.2f}".format(final_payoff)


    def vars_for_template(self):
        player_prefs = [i[0] for i in self.participant.vars['player_prefs']]
        success11 = [i for i in self.participant.vars['success11']]

        return {
                'player_prefs': player_prefs,
                'success11': success11,
                'indices': [j for j in range(1, Constants.nr_courses + 1)],
                'val11': self.participant.vars['val11']
                }


class Thanks(Page):
    pass


page_sequence = [
    Decision,
    ResultsWaitPage,
    Results,
]

#if Constants.application_framing:
 #   if Constants.instructions:
  #      page_sequence.insert(0, InstructionsFramed)

   # if Constants.results:
    #    page_sequence.insert(-1, Results)

#else:
 #   if Constants.instructions:
  #      page_sequence.insert(0, Instructions)

   # if Constants.results:
    #    page_sequence.insert(-1, Results)
