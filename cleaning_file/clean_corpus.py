# -*- coding: utf-8 -*-

def clean_text(input_file, output_file):
    # List of lines to remove
    
    lines_to_remove = {
        "(888) 488-1391",
        "Do I Have A Case?",
        "Let�~@~Ys Chat",
        "Twitter-blue",
        "Instagram-blue",
        "Tiktok-blue",
        "Youtube-blue",
        "LinkedIn-blue",
        "City of Angels",
        "California’s Powerhouse Accident Lawyers With a consecutively proven track record",
        "Disclaimer: Not every one of our firm’s attorneys has received the recognitions stated here. Visit the attorneys’ specific profile page under the ‘Our Firm’ tab for specific attorney recognitions.",
        "Let’s Chat",
        "2960 Wilshire Blvd.Los Angeles, CA 9001024hr Local Line: (213) 277-587824hr Local Line: (310) 277-7529Available by appointment only",
        "The Capitol",
        "333 University Ave. #200Sacramento, CA 9582524hr Local Line: (916) 414-9552Available by appointment only",
        "The Bay Area",
        "505 Montgomery St. #1000San Francisco, CA 9411124hr Local Line: (415) 969-7799Available by appointment only",
        "The Valley",
        "15233 Ventura Blvd. #500Sherman Oaks, CA 9140324hr Local Line: (818) 696-4440Available by appointment only",
        "The Silicon Valley",
        "99 South Almaden Blvd. #600San Jose, CA 9511324hr Local Line: (408) 766-3161Available by appointment only",
        "The City of Trees",
        "11801 Pierce St. #200Riverside, CA 9250524hr Local Line: (951) 530-4659Available by appointment only",
        "The City with Sol",
        "3111 Camino Del Rio N. #400San Diego, CA 9210824hr Local Line: (619) 431-4840Available by appointment only",
        "The Crown City",
        "185 N. Hill Ave. #201Pasadena, CA 9110624hr Local Line: (626) 723-3933Available by appointment only",
        "This website is for informational purposes only and does not provide legal advice. Please do not act or refrain from acting based on anything you read on this site. Using this site or communicating with the law offices of arash khorsandi through this site does not form an attorney/Client relationship. This site is legal advertising.",
        "Copyright © 2025 The Law Office of Arash Khorsandi. All Rights Reserved.",
        "Disclaimer | Privacy Policy | Accessibility | Careers",
        "WE’VE RECOVERED OVER $500 MILLION FOR OUR CLIENTS",
        "Thank You, We’ll contact you shortly."
    }

    # Open input file and process in one pass
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            stripped_line = line.strip()
            if stripped_line and stripped_line not in lines_to_remove:
                outfile.write(line)

    print(f"Processed text saved to {output_file}")

# Define file names
input_filename = "riv_corpus.txt"
output_filename = "cleaned_corpus.txt"

# Run the function
clean_text(input_filename, output_filename)
