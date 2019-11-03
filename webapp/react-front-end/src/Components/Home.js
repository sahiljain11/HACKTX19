import React from 'react'
import Form from "./Form";

export default (props) =>
    <div className="App">
        <div className={"App-center-wrapper"}>
            <div className={"App-center"}>
                <header className={"App-header"}>
                    <h1 className={"Header-title"}>HURRICANE HERO</h1>
                    <p>The greatest weather damage analyzer on Earth. Period.</p>
                </header>

                {/*<p>testing {this.state.username}</p>*/}
            </div>
        </div>
        <Form onChange={props.onChange}/>
    </div>