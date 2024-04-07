use pyo3::prelude::*;
use pyo3::Python;
use pyo3::types::{PyDict, PyList};

#[pyfunction]
fn gen_cyclic_table(py: Python, n_elements: usize) -> PyResult<PyObject> {
    let table = PyDict::new(py);
    
    for i in 0..n_elements {
        let mut row = Vec::new();
        for j in 0..n_elements {
            row.push((j + i) % n_elements);
        }
        let py_row: PyObject = PyList::new(py, &row).to_object(py);
        table.set_item(i.to_object(py), py_row)?;
    }

    Ok(table.into())
}

#[pymodule]
fn gen_cyclic_cayley(_py: Python, m: &PyModule) -> PyResult<()> {
    // Corresponding Python module.
    m.add_function(wrap_pyfunction!(gen_cyclic_table, m)?)?;
    Ok(())
}


