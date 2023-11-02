use rand::Rng;
use std::collections::BinaryHeap;



macro_rules! measure_time {
    ($a:expr) => {{
        for _ in 0..10{
            let mut x = random_vec(1000);
            let start_time = std::time::Instant::now();
            $a(&mut x);
            let end_time = std::time::Instant::now();
            let elapsed_time = end_time - start_time;
            print!("{} ", elapsed_time.as_nanos());
        }
        println!();
    }};
}

fn main() {
    measure_time!(bubble_sort);
    measure_time!(insertion_sort);
    measure_time!(quick_sort);
    measure_time!(merge_sort);
    measure_time!(heap_sort);
    measure_time!(bucket_sort)
}

fn random_vec(size:usize) ->  Vec<i32> {
    let mut r = rand::thread_rng();
    (0..size).map(|_x| r.gen_range(1..1000)).collect()
}

fn bubble_sort<T: Ord>(arr: &mut [T]) {
    let len = arr.len();
    let mut swapped;

    loop {
        swapped = false;

        for i in 0..len - 1 {
            if arr[i] > arr[i + 1] {
                arr.swap(i, i + 1);
                swapped = true;
            }
        }

        if !swapped {
            break;
        }
    }
}

fn insertion_sort<T: Ord>(arr: &mut Vec<T>) {
    for i in 1..arr.len() {
        let mut j = i;

        while j > 0 && arr[j] < arr[j - 1] {
            arr.swap(j, j - 1);
            j -= 1;
        }
    }
}

pub fn quick_sort<T:Ord>(arr: &mut [T]) {
    let len = arr.len();
    _quick_sort(arr, 0, (len - 1) as isize);
}

fn _quick_sort<T:Ord>(arr: &mut [T], low: isize, high: isize) {
    if low < high {
        let p = partition(arr, low, high);
        _quick_sort(arr, low, p - 1);
        _quick_sort(arr, p + 1, high);
    }
}

fn partition<T:Ord>(arr: &mut [T], low: isize, high: isize) -> isize {
    let pivot = high as usize;
    let mut store_index = low - 1;
    let mut last_index = high;

    loop {
        store_index += 1;
        while arr[store_index as usize] < arr[pivot] {
            store_index += 1;
        }
        last_index -= 1;
        while last_index >= 0 && arr[last_index as usize] > arr[pivot] {
            last_index -= 1;
        }
        if store_index >= last_index {
            break;
        } else {
            arr.swap(store_index as usize, last_index as usize);
        }
    }
    arr.swap(store_index as usize, pivot as usize);
    store_index
}					

fn merge<T:Ord + Copy>(x1: &[T], x2: &[T], y: &mut [T]) {
    assert_eq!(x1.len() + x2.len(), y.len());
    let mut i = 0;
    let mut j = 0;
    let mut k = 0;
    while i < x1.len() && j < x2.len() {
        if x1[i] < x2[j] {
            y[k] = x1[i];
            k += 1;
            i += 1;
        } else {
            y[k] = x2[j];
            k += 1;
            j += 1;
        }
    }
    if i < x1.len() {
        y[k..].copy_from_slice(&x1[i..]);
    }
    if j < x2.len() {
        y[k..].copy_from_slice(&x2[j..]);
    }
}

fn merge_sort<T:Ord + Copy>(x: &mut [T]) {
	let n = x.len();
	let m = n / 2;
 
	if n <= 1 {
		return;
	}
 
	merge_sort(&mut x[0..m]);
	merge_sort(&mut x[m..n]);
 
	let mut y: Vec<T> = x.to_vec();
 
	merge(&x[0..m], &x[m..n], &mut y[..]);
 
	x.copy_from_slice(&y);
}


fn heap_sort<T: Ord + Clone>(arr: &mut [T]) {
    let mut heap = BinaryHeap::from(arr.to_vec());

    for i in (0..arr.len()).rev() {
        if let Some(max) = heap.pop() {
            arr[i] = max;
        }
    }
}

fn bucket_sort(arr: &mut [i32]) {
    let min = *arr.iter().min().unwrap();
    let max = *arr.iter().max().unwrap();

    let bucket_count = (max - min) + 1;
    let mut buckets: Vec<Vec<i32>> = vec![Vec::new(); bucket_count as usize];

    for &element in arr.iter() {
        let index = (element - min) as usize;
        buckets[index].push(element);
    }
    let mut index = 0;
    for mut bucket in buckets {
        insertion_sort(&mut bucket);
        for element in bucket {
            arr[index] = element;
            index += 1;
        }
    }
}

