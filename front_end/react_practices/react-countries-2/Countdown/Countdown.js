import { useState, useEffect, useContext } from "react";
import { Color } from "../ColorContext/ColorContext";

export default function Countdown({ seconds, onCountdownFinished }) {
  const [timeLeft, setTimeLeft] = useState(seconds);
  const contextColor = useContext(Color);

  // useEffect(() => {
  //     console.log('calling useEffect', timeLeft)
  //     if (timeLeft === 0) {
  //         onCountdownFinished()
  //     }
  //     const timerId = setTimeout(() => {
  //       setTimeLeft((t) => t - 1);
  //     // setTimeLeft(timeLeft-1);
  //   }, 1000);
  //   console.log('set timeout', timerId)

  //   // we have to provide clean-up function to stop interval/timer!
  //   return () => {
  //     console.log('calling clearTimeout for timerId', timerId)
  //     clearTimeout(timerId)
  //   };
  // }, [timeLeft]);

  useEffect(() => {
    console.log("calling useEffect", timeLeft);
    if (timeLeft == 0) {
      onCountdownFinished();
    } else {
      const intervalId = setInterval(() => {
        console.log("still running interval");
        setTimeLeft((t) => t - 1);

      }, 1000);
      console.log("set intervalId", intervalId);
      return () => {
        console.log("calling clearTimeout for intervalId", intervalId);
        clearInterval(intervalId);
      };
    }
  }, [timeLeft]);
  console.log(contextColor);
  return <div style={{ 'color': contextColor }}>{timeLeft}s</div>;
}
