package training.dev.clapapp

import android.media.MediaPlayer
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.widget.Button
import android.widget.SeekBar
import android.widget.TextView
import com.google.android.material.floatingactionbutton.FloatingActionButton

class MainActivity : AppCompatActivity() {

    private var mediaPlayer: MediaPlayer? = null
    private lateinit var seekBar: SeekBar
    private lateinit var runnable: Runnable
    private lateinit var handler: Handler

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        seekBar = findViewById(R.id.sbClapping) // in this case type is not needed here with <>
        // because explicit type already declared in object definition with SeekBar
        handler = Handler(Looper.getMainLooper())

        val playBtn = findViewById<FloatingActionButton>(R.id.fabPlay)
        val pauseBtn = findViewById<FloatingActionButton>(R.id.fabPause)
        val stopBtn = findViewById<FloatingActionButton>(R.id.fabStop)

        playBtn.setOnClickListener {
            if(mediaPlayer==null){
                mediaPlayer = MediaPlayer.create(this, R.raw.applauding)
                initializeSeekBar()
            }

            mediaPlayer?.start()
        }
        pauseBtn.setOnClickListener {
            mediaPlayer?.pause()
        }
        stopBtn.setOnClickListener {
            mediaPlayer?.stop()

            // Reset + Release mediaPlayer
            mediaPlayer?.reset()
            mediaPlayer?.release()
            mediaPlayer = null
            handler.removeCallbacks(runnable)
            seekBar.progress = 0
        }
    }

    // Reminder
    // Private : can be viewed/called only by components within class
    // Protected : can be viewed/called only by components within class and deriving classes
    // Public : default when nothing specified, can be viewed/called by any components

    private fun initializeSeekBar(){
        seekBar.setOnSeekBarChangeListener(object: SeekBar.OnSeekBarChangeListener{
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                if(fromUser) mediaPlayer?.seekTo(progress)
            }

            override fun onStartTrackingTouch(p0: SeekBar?) {
            }

            override fun onStopTrackingTouch(p0: SeekBar?) {
            }

        })

        val tvPlayed = findViewById<TextView>(R.id.tvPlayed)
        val tvDue= findViewById<TextView>(R.id.tvDue)

        seekBar.max = mediaPlayer!!.duration // !! null check "not null assertion operator"
        runnable = Runnable {
            seekBar.progress = mediaPlayer!!.currentPosition

            val playedTime = mediaPlayer!!.currentPosition/1000
            tvPlayed.text = "$playedTime sec"
            val duration = mediaPlayer!!.duration/1000
            val dueTime = duration - playedTime
            tvDue.text = "$dueTime sec"

            handler.postDelayed(runnable,1000)
        }
        handler.postDelayed(runnable,1000)
    }
}