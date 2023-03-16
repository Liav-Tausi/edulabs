import { Box } from "@mui/system";
import { useState } from "react";
import Countdown from "./Countdown";

export default function CountdownPage() {
  const [seconds, setSeconds] = useState(0);
  const [timerStarted, setTimerStarted] = useState(false);
  const [timerFinished, setTimerFinished] = useState(false);

  const handleStartCountdown = (s) => {
    setSeconds(s);
    setTimerStarted(true);
    setTimerFinished(false);
  };

  const handleCountdownFinished = () => {
    setTimerFinished(true);
  };

  return (
    <>
      <div>Set the countdown time in seconds:</div>
      <form
        onSubmit={(event) => {
          event.preventDefault();
          handleStartCountdown(seconds);
        }}
      >
        <input
          type="number"
          value={seconds}
          onChange={(event) => setSeconds(event.target.value)}
        />
        <button type="submit">Start Countdown</button>
      </form>
      {timerStarted && (
        <Box>
          <Countdown
            key={seconds}
            seconds={seconds}
            onCountdownFinished={handleCountdownFinished}
          />
          {timerFinished && <div>Countdown finished!</div>}
        </Box>
      )}
    </>
  );
}
