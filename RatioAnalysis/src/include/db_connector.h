#ifndef DB_CONNECTOR_H
#define DB_CONNECTOR_H

#include <string>
#include <vector> 
#include <map>
#include "sqlite3.h"

struct FinancialData {
    std::string ticker;
    std::string date;
    double revenue;
    double net_income;
    double t_assets;
    double t_debt;
};

class DBConnector
{
private:
    sqlite3* db;
    std::string dbPath;
public:
    DBConnector(const std::string& path);
    ~DBConnector();

    bool connect();
    void disconnect();

    std::vector<FinancialData> getFinancialData(const std::string& ticker);
    std::vector<std::string> getAvailableTickers();

};


#endif
