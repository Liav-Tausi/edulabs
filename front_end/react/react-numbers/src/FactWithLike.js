import { Button, IconButton, Stack } from "@mui/material";
import ThumbUpAltIcon from '@mui/icons-material/ThumbUpAlt';

export default function FactWithLike(props) {

    return(
        <Stack direction="row" spacing={2} alignItems='center' sx={{justifyContent: "center"}}>
            <p style={{margin: 0}}>{props.factText}</p>
            <IconButton 
                color="primary" variant="outlined" disabled={Boolean(props.isLastNum)}
                onClick={() => {
                  const num = Number(props.factText.split(' ')[0])
                  props.onLikedNumber(num)
                  }
                }>
                <ThumbUpAltIcon />
            </IconButton>
        </Stack>
    )
}