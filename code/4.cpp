/*
    Acredito que a ideia seja fazer o Merge dos 2 arrays e depois fazer a mediana das medianas
    Problema: so para "juntar" os arrays, a complexidade ja seria (m + n)
*/
class Solution {
public:     // Vou tentar fazer um "merge" mas não dos 2 vetores inteiros, somente até preencher um vetor m+n/2

    double merge(vector<int>& nums1, vector<int>& nums2, int& a, int&b){
        if(a < nums1.size() && b < nums2.size()){    // passa pro próximo index do menor
            if(nums1[a] < nums2[b]){
                return nums1[a++];
            }
            else{
                return nums2[b++];
            }
        }
        else if(b >= nums2.size()){
            return nums1[a++];
        }
        else{
            return nums2[b++];
        }
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int totalSize = nums1.size() + nums2.size();
        bool isOddMediam = bool(totalSize & 1); // se par = 0, se nao 1
        // cout << isOddMediam;

        int a = 0, b = 0;
        if(!isOddMediam){
            cout << "Par";
            for(int h = 0; h < ((nums1.size() + nums2.size()) / 2) - 1; h++){  // Para 1 antes dos 2 que vão ser a mediana  
                merge(nums1, nums2, a, b);
                cout << "\nh = " << h;
            }
                // Aqui p a e b vai ter o index anterior a mediana:
            double x, y;
            x = merge(nums1, nums2, a, b);
            y = merge(nums1, nums2, a, b);
            return (x + y) / 2;
        }
        else{
            cout << "Impar";
            for(int h = 0; h < ((nums1.size() + nums2.size()) / 2); h++){  //Para 1 antes da mediana
                merge(nums1, nums2, a, b);
                cout << "\nh = " << h;
            }
            int x;
            x = merge(nums1, nums2, a, b);
            return x;
        }
        return 0.0;
    }

};
