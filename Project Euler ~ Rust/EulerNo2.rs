fn fib(x:usize) -> usize {
    let mut fiblist = [0; 100];
    if x == 0 {fiblist[x]=0; return 0; }
    else if x == 1 {fiblist[x]=1; return 1; }
    else if x == 2 {fiblist[x]=2; return 2; }
    else if fiblist[x] != 0 { return fiblist[x]; }
    else { fiblist[x] = fib(x-1) + fib(x-2); return fiblist[x]; }
}  

fn main() {

let mut result = 0;
let mut i = 0;

while fib(i) < 4000000 {
    if fib(i) % 2 == 0 {
        result += fib(i); }
    i+=1; }

println!("The answer is {}", result); }