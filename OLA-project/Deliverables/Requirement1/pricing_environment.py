import numpy as np
class PricingEnvironment:
    def __init__(self, norm_distribution, cost):
        self.norm_distribution=norm_distribution
        self.cost = cost

    def round(self, p_t,num_cust):
        d_t = np.random.binomial(num_cust,self.norm_distribution(p_t))
        r_t = (p_t-self.cost)*d_t
        return d_t, r_t

def get_expected_profit(curve,cost,prices):
    num=curve(prices)
    profit=num*(prices-cost)
    return np.max(profit)
