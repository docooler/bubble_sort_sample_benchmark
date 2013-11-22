def bubble_sort(arr)  
  1.upto(arr.length-1) do |i|  
    (arr.length-i).times do |j|  
      if arr[j]>arr[j+1]  
        arr[j],arr[j+1] = arr[j+1],arr[j]  
      end  
    end  
  end  
    arr  
end  
  
array = [4, 88, 5, 21, 92, 37, 56, 13, 75, 19, 64, 57, 94, 34, 8, 12, 71, 99, 102, 38] 

bubble_sort(array)