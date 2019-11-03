import React from 'react';
import '../styles/App.css';
import Form from "./Form";

class App extends React.Component {

    state = {
        uploading: false,
        received: false,
        prediction: 0,
        classification: ""
    }

    onChange = e => {
        const files = Array.from(e.target.files)
        this.setState({uploading: true})

        const formData = new FormData()
        //
        // formData.append("0", files[0])
        // console.log(files[0])
        fetch(`${"https://image-classification.cognitiveservices.azure.com/customvision/v3.0/Prediction/2744fc95-61ce-4f3a-a4d6-e0fad1647c9c/classify/iterations/Iteration3/url"}`, {
            method: 'POST',
            body: {"Url": "https://cbsnews1.cbsistatic.com/hub/i/2018/09/12/96f981d8-2b5f-4bde-a092-8ea3aa621af9/florence3.jpg"},
            'Prediction-Key': 'ba8e403c3f904d85adf408928b13fa90',
            'Content-Type': 'application/json'
        })
            .then(res => res.json())
            .then(data => {
                console.log(data)
                this.setState({
                    received: true
                })
            })
    }

    render() {
        const {uploading, received, prediction, classification} = this.state

        const content = () => {
            switch (true) {
                case uploading:
                    return <div>hol up</div>
                case received:
                    return <div>halp me, I gotz the images</div>;
                default:
                    return (
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
                            <Form onChange={this.onChange}/>
                        </div>
                    )
            }
        };

        return (
            <div>
                {content()}
            </div>
        )
    }
}

export default App;
