
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class p5b_mechanism(Page):
    form_model = 'player'


class p6b_example(Page):
    form_model = 'player'


class p7b_ctrq_1(Page):
    form_model = 'player'
    form_fields = ['ctrq1_ttc', 'ctrq2_ttc']

class p7b_ctrq_1_correct(Page):
    def is_displayed(self):
        if self.player.ctrq1_ttc==4 and self.player.ctrq2_ttc==0:
            return True
        else:
            return False

class p7b_ctrq_1_false0(Page):
    def is_displayed(self):
        if self.player.ctrq1_ttc==4 and self.player.ctrq2_ttc!=0:
            return True
        else:
            return False

class p7b_ctrq_1_false4(Page):
    def is_displayed(self):
        if self.player.ctrq1_ttc!=4 and self.player.ctrq2_ttc==0:
            return True
        else:
            return False

class p7b_ctrq_1_false_both(Page):
    def is_displayed(self):
        if self.player.ctrq1_ttc!=4 and self.player.ctrq2_ttc!=0:
            return True
        else:
            return False


class p7b_ctrq_2(Page):
    form_model = 'player'
    form_fields = ['ctrq3_ttc_blue', 'ctrq3_ttc_yellow', 'ctrq3_ttc_orange', 'ctrq3_ttc_purple']
    timeout_seconds = Constants.timer_seconds
    def before_next_page(self):
        self.player.time_left = self.timeout_seconds

    def vars_for_template(self):
        return {
            'timeout_seconds': self.timeout_seconds
        }

class p7b_ctrq_2_correct(Page):
    def is_displayed(self):
        if self.player.ctrq3_ttc_blue=='A' and self.player.ctrq3_ttc_yellow=='C' and self.player.ctrq3_ttc_orange=='D' and self.player.ctrq3_ttc_purple=='B':
            return True
        else:
            return False

class p7b_ctrq_2_false(Page):
    def is_displayed(self):
        if self.player.ctrq3_ttc_blue!='A' or self.player.ctrq3_ttc_yellow!='C' or self.player.ctrq3_ttc_orange!='D' or self.player.ctrq3_ttc_purple!='B':
            return True
        else:
            return False

class p7b_mc(Page):
    form_model = 'player'
    form_fields = ['mc1_ttc', 'mc2_ttc', 'mc3_ttc', 'mc4_ttc']


class p8b_info_decision_start(Page):
    form_model = 'player'


page_sequence = [p5b_mechanism, p6b_example, p7b_ctrq_1, p7b_ctrq_1_correct, p7b_ctrq_1_false0, p7b_ctrq_1_false4,
                 p7b_ctrq_1_false_both, p7b_ctrq_2, p7b_ctrq_2_correct, p7b_ctrq_2_false, p7b_mc, p8b_info_decision_start]