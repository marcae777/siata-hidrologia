import React from 'react'
import './TitleButton.css';

class TitleButton extends React.Component {
  render() {
    const {title} = this.props;
    console.log(title)
    return (
      <div className = "TitleButton">
        <div className={title}>
          {title}
        </div>
      </div>
    );
  }
}

export default TitleButton;
