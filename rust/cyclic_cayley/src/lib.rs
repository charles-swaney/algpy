use pyo3::prelude::*;
use pyo3::Python;
use pyo3::types::PyDict;

#[pyfunction]
fn gen_cyclic_table(py: Python, n_elements: usize) -> PyResult<PyObject> {
    let table = PyDict::new(py);
    for i in 0..n_elements {
        let row = PyDict::new(py);
        for j in 0..n_elements {
            let value = ((i + j) % n_elements).to_object(py);
            row.set_item(j, &value)?;
        }
        table.set_item(i.to_object(py), row)?;
    }
    Ok(table.into())
}

#[pymodule]
fn gen_cyclic_cayley(_py: Python, m: &PyModule) -> PyResult<()> {
    // Corresponding Python module.
    m.add_function(wrap_pyfunction!(gen_cyclic_table, m)?)?;
    Ok(())
} 
