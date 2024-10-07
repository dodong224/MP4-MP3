from moviepy.editor import VideoFileClip
import os

def convert_mp4_to_mp3():
    try:
        # Get input file path
        video_path = input("Enter the path to your MP4 file: ").strip('"')
        
        # Check if file exists and is MP4
        if not os.path.exists(video_path):
            print("Error: File does not exist.")
            return False
        
        if not video_path.lower().endswith('.mp4'):
            print("Error: File is not an MP4.")
            return False
            
        # Ask for confirmation
        ready = input("Ready for conversion? (yes/no): ").lower()
        if ready != 'yes':
            print("Conversion cancelled.")
            return False
            
        # Generate output path
        output_path = os.path.splitext(video_path)[0] + '.mp3'
        
        # Convert video to audio
        print("Converting MP4 to MP3...")
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_path)
        
        # Clean up
        audio_clip.close()
        video_clip.close()
        
        # Check if conversion was successful
        if os.path.exists(output_path):
            print(f"\nSuccess! Audio saved to: {output_path}")
            return True
        else:
            print("\nError: Conversion failed.")
            return False
            
    except Exception as e:
        print(f"\nError during conversion: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure the input file is a valid MP4 video")
        print("2. Check if you have write permissions in the output directory")
        print("3. Ensure you have enough disk space")
        print("4. Verify that the input path is correct")
        return False

def main():
    print("=== MP4 to MP3 Converter ===")
    
    # Check if moviepy is installed
    try:
        import moviepy
    except ImportError:
        print("Error: moviepy library is not installed.")
        print("Please install it using: pip install moviepy")
        return
    
    # Run conversion
    success = convert_mp4_to_mp3()
    
    if not success:
        print("\nConversion process ended with errors.")
    
    print("\nProgram finished.")

if __name__ == "__main__":
    main()
