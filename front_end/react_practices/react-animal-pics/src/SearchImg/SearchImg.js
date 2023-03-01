import '../SearchImg/SearchImg.css'
import '../SearchObj/SearchObj.css'


const SearchImg = (props) => {
    
  return(
    <div className="container2">
      <img className="imgs" src={props.imgUrl} alt="animal"/>
    </div>
  );

}

export default SearchImg;