fn euler1() {
   
   let mut sum = 0;
   
   for x in 1..1000 {
        if x % 3 == 0 || x % 5 == 0 {
        sum += x; }  }
        

    println!("The answer is: {}", sum); }

fn main() {
euler1(); }