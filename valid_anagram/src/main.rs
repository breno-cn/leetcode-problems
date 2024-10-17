pub fn is_anagram(s: String, t: String) -> bool {
    let mut count_s: [i32; 26] = [0; 26];
    let mut count_t: [i32; 26] = [0; 26];
    let base_value = 'a' as u8;

    for c in s.into_bytes() {
        count_s[(c - base_value) as usize] += 1;
    }

    for c in t.into_bytes() {
        count_t[(c - base_value) as usize] += 1;
    }

    count_s == count_t
}

fn main() {
    println!(
        "{:}",
        is_anagram("a".to_string(), "ab".to_string())
    );
}
