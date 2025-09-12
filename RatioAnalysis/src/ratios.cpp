#include <iostream>
#include "ratios.h"

explicit ratio::ratio () : 
    sales (0.0),
    net_income (0.0),
    t_assets (0.0),
    f_assets (0.0),
    c_assets (0.0),
    debt (0.0),
    c_debt (0.0),
    f_debt (0.0),
    equity (0.0),
    credit_sales (0.0),
    avg_daily_credit_sales (0.0),
    acc_receivables (0.0),
    inventory (0.0),
    fixed_charges (0.0),
    interest (0.0),
    ebit (0.0), //earnings before interest and taxes
    gross_profit(0.0), //earnings before fixed charges and taxes
    debt_to_total_a (0.0),
    times_interest_earned (0.0),
    fixed_charge_coverage (0.0),
    current_ratio (0.0),
    quick_ratio (0.0),  
    receiv_turnover (0.0),
    avg_collection_period (0.0),
    inventory_turnover (0.0),
    f_asset_turnover (0.0),
    t_asset_turnover (0.0),
    profit_margin (0.0),
    roe (0.0),
    roa (0.0) //return on assets
{} //return on equity

double ratio::read() const { 
    std::cout << "Return on equity: " << roe << "\nReturn on assets: " << roa 
    << "\nProfit margin: " << profit_margin << "\nTotal Asset Turnover: " << t_asset_turnover << "\nFixed Asset Turnover: "
    << f_asset_turnover << "\nInventory Turnover" << inventory_turnover << "\nAverage Collection Period: " << avg_collection_period
    << "\nReceivables Turnover: " << receiv_turnover << "\nCurrent Ratio: " << current_ratio << "\nQuick Ratio: " << quick_ratio
    << "\nFixed Charge Coverage: " << fixed_charge_coverage << "\nTimes Interest Earned: " << times_interest_earned 
    << "\nDebt-to-Total Assets: " << debt_to_total_a << std::endl;
    return 0;
}


void ratio::calculations(){
    roe = net_income/equity;
    roa = net_income/t_assets;
    profit_margin = net_income/sales;
    t_asset_turnover = sales/t_assets;
    f_asset_turnover = sales/f_assets;
    inventory_turnover = sales/inventory;
    avg_daily_credit_sales = credit_sales/365;
    avg_collection_period = acc_receivables/avg_daily_credit_sales;
    receiv_turnover = credit_sales/acc_receivables;
    current_ratio = c_assets/c_debt;
    quick_ratio = (c_assets-inventory)/c_debt;
    fixed_charge_coverage = gross_profit/fixed_charges;
    times_interest_earned = ebit/interest;
    debt_to_total_a = debt/t_assets;
}

double ratio::read_roe() const{
    return roe;
}
double ratio::read_roa() const{
    return roa;
}
double read_profit_margin() const;
double read_t_asset_turnover() const;
double read_f_asset_turnover() const;
double read_inventory_turnover() const;
double read_avg_collection_period() const;
double read_receiv_turnover() const;
double read_quick_ratio() const;
double read_current_ratio() const;
double read_fixed_charge_coverage() const;
double read_times_interest_earned() const;
double read_debt_to_total_a() const; 
