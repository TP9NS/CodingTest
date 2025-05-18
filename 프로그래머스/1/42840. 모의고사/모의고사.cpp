#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int c1=0;
int c2=0;
int c3=0;

vector<int> solution(vector<int> answers) {
    const int one[5] ={1,2,3,4,5};
    const int two[8] ={2,1,2,3,2,4,2,5};
    const int three[10] ={3,3,1,1,2,2,4,4,5,5};
    
    vector<int> answer;
    
    for (size_t i=0; i<answers.size();i++){
        int one_index= i%(sizeof(one)/sizeof(int));
        int two_index= i%(sizeof(two)/sizeof(int));
        int three_index= i%(sizeof(three)/sizeof(int));
        
        if(one[one_index]==answers[i]){
            c1+=1;
        }
        if(two[two_index]==answers[i]){
            c2+=1;
        }
        if(three[three_index]==answers[i]){
            c3+=1;
        }
    }
    int max_score = max({c1, c2, c3});

    if (c1 == max_score) answer.push_back(1);
    if (c2 == max_score) answer.push_back(2);
    if (c3 == max_score) answer.push_back(3);
    return answer;
}