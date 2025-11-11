class Solution {
public:
    int mediana(vector<int>& v){
        sort(v.begin(), v.end());
        return v[v.size()/2];
    }
    vector<vector<int>> separarColunas(vector<int>& v){
        vector<vector<int>> colunas;
        for (int i = 0; i < v.size(); i += 5) {
            int fim = min(i + 5, (int)v.size());
            vector<int> coluna(v.begin() + i, v.begin() + fim);
            colunas.push_back(coluna);
        }
        return colunas;
    }
    int medianaDasMedianas(vector<vector<int>>& colunas){

        if(colunas.size() == 1){
            return mediana(colunas[0]);
        }

        vector<int> medianas(colunas.size(), 0);
        for(int i = 0; i < medianas.size(); i++){
            medianas[i] = mediana(colunas[i]);
        }

        vector<vector<int>> novasColunas = separarColunas(medianas);
        return medianaDasMedianas(novasColunas);
    }

    int findK(vector<int>&nums, int k){
        int pivo;
        vector<vector<int>> colunas = separarColunas(nums);
        pivo = medianaDasMedianas(colunas);
    
        vector<int> menores, iguais, maiores;
        for (int x : nums) {
            if (x > pivo)
                maiores.push_back(x);
            else if (x < pivo)
                menores.push_back(x);
            else
                iguais.push_back(x);
        }
        if (k <= maiores.size())              
            return findK(maiores, k);
        else if (k <= maiores.size() + iguais.size()) 
            return pivo;
        else                                  
            return findK(menores, k - maiores.size() - iguais.size());
    }
    int findKthLargest(vector<int>& nums, int k) {
        int kMaior;
        kMaior = findK(nums, k);

        return kMaior;
    }
};
