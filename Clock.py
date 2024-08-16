# mins = int(input())
# days = mins//1440
# clock = (mins%1440)//60
# minats = (mins%1440)%60
# while days<30:
#     if days<10: 
#         days = '0' + str(days)
#     if clock<10: 
#         clock = '0' + str(clock)
#     if minats<10:
#         minats = '0' + str(minats)
#     print(f'{days}:{clock}:{minats}')



"""q = input("Введите числа через запитую: ")
print(f'Исходная строка - "{q}"')
q = q.split(',')
for i in q:
    print(f'Новые строки созданные из исходной = "{i}"')
r=0
счётчик_прохода_цикла=0
for i in q:
    print(f'    Начало цикла')
    print(f'Строка i= "{i}"')
    e = int(i)
    print(f'Число e=i = {e}')
    r +=e
    print(f'Прибавление поочерёдное всех чисел исходной строки = {r}')
    счётчик_прохода_цикла += 1
    print(f'    Цикл прошёл {счётчик_прохода_цикла} раз.')
print(f'    Конец цикла, цикл прошёл {счётчик_прохода_цикла}, который равен колличеству цифр в исходной строке.')
print(f'    Сумма всех чисел в изначальной строке = {r}')"""

"""class Solution{
    public boolean searchMatrix(int[][] matrix, int k){
        if (matrix == null || matrix.lenght == 0 || matrix[0].lenght == 0){
            return false;
        }
        int m = matrix.lenght, n = matrix[0].lenght;
        int i = 0, j = n - 1;
        while (i < m && j>=0){
            if (matrix[i][j] == k){
                return true;
            }
            if (matrix[i][j] > k){
                j--;
            } else {
                i++;
            }
        }
        return false;
    }
}"""


def search_matrix(matrix, k):
    """
    Проверяет, существует ли элемент k в двумерной матрице.
    
    Args:
    matrix (list[list[int]]): Двумерная матрица, в которой необходимо искать элемент.
    k (int): Искомый элемент.
    
    Returns:
    bool: True, если элемент найден, False в противном случае.
    """
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n - 1
    
    while i < m and j >= 0:
        if matrix[i][j] == k:
            return True
        elif matrix[i][j] > k:
            j -= 1
        else:
            i += 1
    
    return False
print(search_matrix(1,2))