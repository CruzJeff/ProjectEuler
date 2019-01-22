
fn option(){

	//Option<T>

	let x = 3.0;
	let y = 2.0;

	//returns Some(z) or None

	let result:Option<f64> = 
		if y != 0.0 {Some(x/y)} else { None };
	println!("{:?}", result);

	match result {

		Some(z) => println!("{}/{} = {}", x,y,z),
		None => println!("Cannot divide by 0")
	}

}

fn main(){
	option();
}