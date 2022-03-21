import React, { useState } from 'react';

const FormularioUpoad = () => {
    const [file, setFile] = useState(null);
    const [error, setError] = useState(null)

    const types = ['image/png', 'image/jpeg'];


    const changeHandler = (e) => {
        let selected = e.target.files[0];

        if (selected && types.includes(selected.type)) {
            setFile(selected);
        } else {
            setFile(null);
            setError('Por favor selecciona una imagen(png or jpeg)')
        }
    }

    return (
        <form>
            <input type='file' onChange={changeHandler} />
            <div className='output' >
                {error && <div className='error'>{error}</div>}
                {file && <div> {file.name} </div>}
            </div>
        </form>
    )
}

export default FormularioUpoad 