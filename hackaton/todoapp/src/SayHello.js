import React from 'react';
import axios from 'axios';

export default class SayHello extends React.Component {
    state = {
      hello: ''
    }
  
    componentDidMount() {
      axios.get(`http://localhost:8000/hello/`)
        .then(res => {
          const hello = res.data;
          this.setState(hello);
        })
    }
  
    render() {
      return (
          this.state.hello
      )
    }
}