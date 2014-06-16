package main 

// import "fmt"

func bubble_sort(array []int) {
	length := len(array)
	for i:=0; i<length;i++{
		for j := i+1; j < length; j++ {
			if array[j] < array[i] {
				array[j],array[i] = array[i],array[j]
			}
		}
	}
}

func main() {
	arr := [] int{4, 88, 5, 21, 92, 37, 56, 13, 75, 19, 64, 57, 94, 34, 8, 12, 71, 99, 102, 38}
	bubble_sort(arr)
}
