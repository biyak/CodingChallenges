#include <iostream>

int binarySearch(int find, int list[]){
  size_t n = sizeof(list)/sizeof(list[0]);
  return n;
  //std::cout << n;
  
}

int main() {

  int theList[] {1,2,3,4,5,6,7,8};
  int size = binarySearch(9, theList);
  std::cout << "Length:" << size ;
}
