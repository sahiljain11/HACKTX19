import React from 'react'

export default props =>

    <form className={"Input-group"} action={"/result"}>

        <div className={"num-input"}>
            {/*<label htmlFor={"xcoord"}>x: </label>*/}
            <input name={"xcoord"} placeholder={"y: 0.00"} type={"number"}/>
            {/*</div>*/}

            {/*<div className={"num-input"}>*/}
            {/*<label htmlFor={"ycoord"}>y: </label>*/}
            <input name={"ycoord"} placeholder={"x: 0.00"} type={"number"}/>
        </div>

        <div>
            <input type="file" name="file" id="file" className={"Input-file"} accept={"image/*"}
                   alt={"arial photo input"} onChange={props.onChange} required/>
            <label htmlFor="file" className={"Input-name"}
            >Choose a file</label>
            
            {/*<Link to={"/result"}>Link test here</Link>*/}
            <input type={"submit"} className={"Input-name"}/>
            {/*<input type="file" name="pic" id="pic" accept={"image/*"}/>*/}
            {/*<label htmlFor="file">Choose a file</label>*/}
        </div>
    </form>