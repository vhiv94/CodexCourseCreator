


// Ascii art logo!!!
// raw string: r#""#
const LOGO: &str = r#"
   __               ____                              
  / /  ___  ___ _  / __/_ ____ _  __ _  ___ _______ __
 / /__/ _ \/ _ `/ _\ \/ // /  ' \/  ' \/ _ `/ __/ // /
/____/\___/\_, / /___/\_,_/_/_/_/_/_/_/\_,_/_/  \_, / 
          /___/                                /___/  
"#; // trim leading and trailing \n
const RULE: &str = "--------------------------------------------------------------------------------";

/// Entry Point
fn main() {

    // macro: expands to interperate variable, print the line to stdout, then an additional \n
    println!("{}", RULE);
    println!("{}", LOGO);
    println!("{}", RULE);
}
