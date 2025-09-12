// Created to check Bollinger Bands by Julius Krüger for Fidus Capital Society [FCS]
// Any rights belong to the creator Julius Krüger and Fidus Capital Society [FCS]
#include <iostream>
#include <vector>
#include <cmath> 


class Boll{
    private:
        int n{0};
        int k{0};
        std::vector<double> schlusswerte{};
        double average{0.0};
        std::vector<double> abweichung{};
        double sum{0.0}; // sum of all schlusswerte
        double sum2{0.0}; // sum of all squared standard deviations 
        double root{0.0}; // sqrt of sum2
        double oberes{0.0};
        double unteres {0.0}; 
    public: 
        explicit Boll () :
            n(0), k(0), average(0.0), sum(0.0), sum2(0.0), root(0.0), oberes(0.0), unteres(0.0) {}
        

        void input_n(int f){ // input for time period n
            n = f;
            schlusswerte.resize(n);
            abweichung.resize(n);
        }
        void input_k(int g){ // input of parameter k 
            k = g;
        }
        void input_schlusswerte(int i, double x){
            schlusswerte[i] = x;
        }
        void calculations(){
            sum = 0.0;
            sum2 = 0.0;

            for(const auto & x : schlusswerte){ //sigma of all end values
                sum += x;
            }
            average = sum/n;
            std::cout << average << std::endl;
            for(int j = 0; j < n; j++){ //subtract average of end values 
                double sd = 0.0;
                sd = schlusswerte[j] - average;
                abweichung[j] = sd*sd; //square diviation
            }
            for(const auto & x : abweichung){ //sigma of standard diviation
                sum2 += x;
            }
            root = sqrt((sum2/n)); // take square root of division of sum of squared standard deviations by length of period n
            oberes = average + root*k; // calc upper band
            unteres = average - root*k; // calc lower band 
        }
        double return_ob() const //return upper band
        {
            return oberes;
        }
        double return_ub() const // return lower band 
        {
            return unteres;
        }

        
};

int main(){
    Boll aktie;
    int n = 0;
    int k = 0;
    bool loop1;
    bool loop = true;

    while(loop) {
        loop1 = true;
        while (loop1)
        {
            std::cout << "Enter length of period (n): ";
            std::cin >> n;
            aktie.input_n(n);
            std::cout << std::endl;
            std::cout << "Enter parameter k: ";
            std::cin >> k;
            aktie.input_k(k);
            std::cout << std::endl;

            char in;
            std::cout << "\nTo change parameters press 'c' – to continue press any other character" << std::endl;
            std::cout << "Input: ";
            std::cin >> in;
            if (in == 'c')
            {
                loop1 = true;
            }
            else{
                loop1 = false;
            }
            
        }
        loop1 = true;
        while(loop1) {
            for (int i = 0; i < n; i++)
            {
                double x = 0.0;
                std::cout << "Closing Price " << i + 1 << ": ";
                std::cin >> x;
                aktie.input_schlusswerte(i, x);
            }
            char in;;
            std::cout << "\nTo change Closing Prices press 'c' – to continue press any other character" << std::endl;
            std::cout << "Input: ";
            std::cin >> in;
            if (in == 'c')
            {
                loop1 = true;
            }
            else{
                loop1 = false;
            }
            
        }

        aktie.calculations();
        std::cout << "\nUpper Band: " << aktie.return_ob() << std::endl;
        std::cout << "Lower Band: " << aktie.return_ub() << std::endl;

        char c;
        std::cout << "\nTo repeat the calculation press 'c' – exit the program by pressing any other key" << std::endl;
        std::cout << "Input: ";
        std::cin >> c;
        if(c == 'c'){
            loop = true;
        }
        else{
            loop = false;
        }
    }
    return 0;
}