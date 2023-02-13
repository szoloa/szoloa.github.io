#include <iostream>

using namespace std;

class Test1
{
    string name;
    public:
        string getname(){
            return name;
        }
        void setname(string name);
        Test1(string);
};
Test1::Test1(string n): name(n)
{

}
int main(){
    Test1 test = Test1("lolo");
    cout <<  "his name is "<< test.getname() << endl;
     return 0;
}