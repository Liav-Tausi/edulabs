
const ImgCounter = (props) => {
  return(
    <>
    <div className="count">total count: {props.totalCount}</div>
    <div className="count">found count: {props.foundCount}</div>
    </>
  )

}

export default ImgCounter;