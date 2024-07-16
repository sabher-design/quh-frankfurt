from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class p5a_mechanism(Page):
    form_model = 'player'

class p6a_example(Page):
    form_model = 'player'

class p7a_ctrq_1(Page):
    form_model = 'player'
    form_fields = ['ctrq1_da', 'ctrq2_da']

class p7a_ctrq_1_correct(Page):
    def is_displayed(self):
        if self.player.ctrq1_da==4 and self.player.ctrq2_da==0:
            return True
        else:
            return False

class p7a_ctrq_1_false0(Page):
    def is_displayed(self):
        if self.player.ctrq1_da==4 and self.player.ctrq2_da!=0:
            return True
        else:
            return False

class p7a_ctrq_1_false4(Page):
    def is_displayed(self):
        if self.player.ctrq1_da!=4 and self.player.ctrq2_da==0:
            return True
        else:
            return False

class p7a_ctrq_1_false_both(Page):
    def is_displayed(self):
        if self.player.ctrq1_da!=4 and self.player.ctrq2_da!=0:
            return True
        else:
            return False

class p7a_ctrq_2(Page):
    form_model = 'player'
    form_fields = ['ctrq3_da_blue', 'ctrq3_da_yellow', 'ctrq3_da_orange', 'ctrq3_da_purple']
    timeout_seconds = Constants.timer_seconds
    def before_next_page(self):
        self.player.time_left = self.timeout_seconds

    def vars_for_template(self):
        return {
            'timeout_seconds': self.timeout_seconds
        }

class p7a_ctrq_2_correct(Page):
    def is_displayed(self):
        if self.player.ctrq3_da_blue=='B' and self.player.ctrq3_da_yellow=='C' and self.player.ctrq3_da_orange=='A' and self.player.ctrq3_da_purple=='D':
            return True
        else:
            return False

class p7a_ctrq_2_false(Page):
    def is_displayed(self):
        if self.player.ctrq3_da_blue!='B' or self.player.ctrq3_da_yellow!='C' or self.player.ctrq3_da_orange!='A' or self.player.ctrq3_da_purple!='D':
            return True
        else:
            return False

class p7a_mc(Page):
    form_model = 'player'
    form_fields = ['mc1_da', 'mc2_da', 'mc3_da', 'mc4_da']

class p8a_info_decision_start(Page):
    form_model = 'player'


page_sequence = [p5a_mechanism, p6a_example, p7a_ctrq_1, p7a_ctrq_1_correct, p7a_ctrq_1_false0, p7a_ctrq_1_false4,
                 p7a_ctrq_1_false_both, p7a_ctrq_2, p7a_ctrq_2_correct, p7a_ctrq_2_false, p7a_mc, p8a_info_decision_start]