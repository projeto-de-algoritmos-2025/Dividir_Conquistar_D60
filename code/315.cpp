/*
Basicamente conto/armazeno quantas inversões tenho que fazer para cada numero chegar na sua pos?

Acredito que a difereça seja que o retorno não é a soma do numero de inversões, e sim um vetor que conta individualmente.

Por força bruta (O(n²)) ==> para cada index, percorro o vetor contando os maiores que nums[i]

Pela lógica do counting inversion (O(n log(n)))
*/

class Solution {
public:

    // Usando uma lógica de MergeSort
    void MergeAndCount(vector<int>& index, vector<int>& inversionCounter, vector<int>& vec, int comeco, int meio, int fim) {

        // vectors auxiliares
        vector<int> merged; 
        vector<int> newIndex;

        int i = comeco, j = meio + 1;
        int rightCount = 0; // conta quantos da direita já são menores que os da esquerda

        while (i <= meio && j <= fim) {
            if (vec[j] < vec[i]) {          // elemento da direita é menor
                merged.push_back(vec[j]);
                newIndex.push_back(index[j]);
                rightCount++;               // ==> incrementa todos os numeros da esquerda >= i
                j++;
            } 
            else {
                // adiciona o número da esquerda e soma quantos menores da direita já passaram
                merged.push_back(vec[i]);
                newIndex.push_back(index[i]);
                inversionCounter[index[i]] += rightCount;
                i++;
            }
        }

        // sobrou elementos na esquerda
        while (i <= meio) {
            merged.push_back(vec[i]);
            newIndex.push_back(index[i]);
            inversionCounter[index[i]] += rightCount;
            i++;
        }

        // na direita
        while (j <= fim) {
            merged.push_back(vec[j]);
            newIndex.push_back(index[j]);
            j++;
        }

        // atualiza o vetor/index original (tira do vetor auxiliar)
        for (int k = 0; k < merged.size(); k++) {
            vec[comeco + k] = merged[k];
            index[comeco + k] = newIndex[k];
        }
    }

    void SortAndCount(vector<int>& index, vector<int>& inversionCounter, vector<int>& vec, int comeco, int fim) {
        if (comeco >= fim)
            return;

        int meio = (comeco + fim) / 2;    // Divisão do vetor

        SortAndCount(index, inversionCounter, vec, comeco, meio);   // Chamada à esquerda
        SortAndCount(index, inversionCounter, vec, meio + 1, fim);  // '' direita

        MergeAndCount(index, inversionCounter, vec, comeco, meio, fim);
        return;
    }

    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> index(n);
        for (int i = 0; i < n; i++) {
            index[i] = i;
        }

        vector<int> inversionCounter(n, 0);
        SortAndCount(index, inversionCounter, nums, 0, n - 1);

        return inversionCounter;
    }
};
