import * as React from 'react';

import PageInterface from '../PageInterface';

class App extends React.Component<PageInterface, {}> {
  render() {
    return (
        <div className="container main">
          <div className="row">
            <div className="jumbotron col-12">
              <div className="container">
                <h1>Hello, world! {this.props.color}</h1>
              </div>
            </div>
          </div>
        </div>
    );
  }
}

export default App;
