import api, coh, overheads, profit_loss

def main():

    forex = api.api_function()
    coh.coh_function(forex)
    overheads.overhead_function(forex)
    profit_loss.profitloss_function(forex)

main()