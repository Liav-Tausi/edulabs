import '../SearchObj/SearchObj.css'
import { useState } from "react";
import { IMG_DATA } from "../IMG_DATA";
import SearchImg from "../SearchImg/SearchImg";
import ImgCounter from "../ImgCounter/ImgCounter";

const SearchObj = () => {
  const [searchText, setSearchText] = useState('');
  const [currImgUrl, setCurrImgUrl] = useState(null);
  const [totalCount, setTotalCount] = useState(0);
  const [foundCount, setFoundCount] = useState(0);
  const [currImgIndex, setCurrImgIndex] = useState(0);

  const handleTextSubmit = (event) => {
    event.preventDefault()
    const animal = searchText.toLowerCase();

    if (animal in IMG_DATA) {
          setCurrImgUrl(IMG_DATA[animal])
          setFoundCount((n) => n + 1)  
          setCurrImgIndex(0);
      } else {
          setCurrImgUrl(null)
          alert('We could not find this image');
      }
      setTotalCount((n) => n + 1)
  }

  const handlePrevImg = () => {
    if (currImgIndex > 0) {
    setCurrImgIndex(currImgIndex - 1);
    }
  }

  const handleNextImg = () => {
    if (currImgIndex < currImgUrl.length - 1) {
    setCurrImgIndex(currImgIndex + 1);
    }
  }

  const handleClearImg = () => {
    setCurrImgUrl(null);
    setSearchText('');
    setCurrImgIndex(0);
  }

  let imageElement = null;
  let counterElement = <ImgCounter totalCount={totalCount} foundCount={foundCount}/>;

  if (currImgUrl !== null) {
    const currImg = currImgUrl[currImgIndex];
    imageElement = (
      <div>
        <SearchImg imgUrl={currImg} />
        {
        currImgUrl.length > 1 &&
        <div className='container2'>
          <button onClick={handlePrevImg} disabled={currImgIndex === 0}>
            <img className="prev" src="https://cdn-icons-png.flaticon.com/512/3916/3916837.png" alt="privios" />
          </button>

          <button onClick={handleNextImg} disabled={currImgIndex === currImgUrl.length - 1}>
            <img className="next" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Feather-arrows-arrow-right.svg/1200px-Feather-arrows-arrow-right.svg.png" alt="next" />
          </button>
        </div>
        }
        <div className="container2">
          <button className="clear-button" onClick={handleClearImg}>Clear</button>
        </div>
      </div>
    );
  }

  return (
    <div className="container">
      <form className="search-form" onSubmit={handleTextSubmit}>
        <label className="search-lable" htmlFor="animal-search-bar">Search animals</label>
        <input className="search-bar" type="text"
          placeholder="Search for animals."
          value={searchText}
          onChange = {(event) => {setSearchText(event.target.value)}}
        />
        <button className="search-button">Search</button>
      </form>

        {counterElement}

        {imageElement}
    </div>
  );
}

export default SearchObj;