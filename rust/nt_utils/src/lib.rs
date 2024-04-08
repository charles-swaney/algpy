use pyo3::prelude::*;
use pyo3::Python;

#[pyfunction]
fn is_prime(n: usize) -> bool {
    // Every prime number >3 is congruent to 1 or -1 mod 6
    if n <= 1 {
        return false
    }
    else if n <= 3 {
        return true
    }
    else if n % 2 == 0 || n % 3 == 0 {
        return false
    }
    let mut curr = 5;
    let upper_limit: usize = (n as f64).sqrt() as usize + 1;
    while curr <= upper_limit {
        if n % curr == 0 || n % (curr + 2) == 0 {
            return false
        }
        curr += 6;
    }
    true
}

#[pymodule]
fn nt_utils(_py: Python, m: &PyModule) -> PyResult<()> {
    // Corresponding Python module.
    m.add_function(wrap_pyfunction!(is_prime, m)?)?;
    Ok(())
} 

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_is_prime() {
        assert_eq!(is_prime(2), true);
        assert_eq!(is_prime(3), true);
        assert_eq!(is_prime(4), false);
        assert_eq!(is_prime(5), true);
        assert_eq!(is_prime(29), true);
        assert_eq!(is_prime(30), false);
    }
}
