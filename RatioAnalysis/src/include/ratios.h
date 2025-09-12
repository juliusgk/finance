#ifndef ratio_H
#define ratio_H


class ratio
{
private:
    double sales {0.0};
    double net_income {0.0};
    double t_assets {0.0};
    double f_assets {0.0};
    double c_assets {0.0};
    double debt {0.0};
    double c_debt {0.0};
    double f_debt {0.0};
    double equity {0.0};
    double fixed_charges {0.0};
    double interest {0.0};
    double roa {0.0}; //return on assets
    double credit_sales {0.0};
    double avg_daily_credit_sales {0.0};
    double acc_receivables {0.0};
    double inventory {0.0};
    double ebit {0.0}; //earnings before interest and taxes
    double gross_profit{0.0}; //earnings before fixed charges and taxes
    double debt_to_total_a {0.0};
    double times_interest_earned {0.0};
    double fixed_charge_coverage {0.0};
    double current_ratio {0.0};
    double quick_ratio {0.0};  
    double receiv_turnover {0.0};
    double avg_collection_period {0.0};
    double inventory_turnover {0.0};
    double f_asset_turnover {0.0};
    double t_asset_turnover {0.0};
    double profit_margin {0.0};
    double roe {0.0}; //return on equity
public:
    void calculations();
    double read() const;
    double read_roe() const;
    double read_roa() const;
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
    
 ratio(/* args */);
     ratio();
};
 ratio:: ratio()
{
}

#endif




