# GolfVilla.com — Destination Page Generator
# Generates 30+ destination-specific golf villa guides
# Output: SEO-Files/ subfolder
# USAGE: python generate_destination_pages.py
# Run from: C:\Users\rbend\Desktop\GOLFVILLA-WEBSITE\Funnel Websites\golfvilla-com\

import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SEO-Files")
os.makedirs(OUTPUT_DIR, exist_ok=True)

NAV = """<nav class="site-nav scrolled" id="main-nav">
  <a href="/" class="nav-logo"><span class="logo-top">Golf Villa</span><span class="logo-sub">The World's Premier Golf Villa</span></a>
  <div class="nav-links">
    <a href="/what-is-a-golf-villa">What is a Golf Villa?</a>
    <a href="/caribbean-golf-villa">Caribbean</a>
    <a href="/cap-cana-golf-villa">Cap Cana</a>
    <a href="/luxury-golf-villa">Luxury</a>
    <a href="https://www.espadavilla.com" class="nav-book-btn">Book Now</a>
  </div>
  <button class="nav-hamburger" aria-label="Open menu"><span></span><span></span><span></span></button>
</nav>
<div class="mobile-menu"><button class="mobile-close">×</button>
  <a href="/">Home</a><a href="/caribbean-golf-villa">Caribbean</a>
  <a href="/cap-cana-golf-villa">Cap Cana</a>
  <a href="https://www.espadavilla.com">Book Villa Espada →</a>
</div>"""

FOOTER = """<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <span class="logo-top">Golf Villa</span>
      <span class="logo-sub">The World's Premier Golf Villa</span>
      <p>GolfVilla.com — the authoritative guide to private golf villa rentals worldwide.</p>
    </div>
    <div class="footer-col"><h4>Explore</h4><ul>
      <li><a href="/what-is-a-golf-villa">What is a Golf Villa?</a></li>
      <li><a href="/caribbean-golf-villa">Caribbean Golf Villas</a></li>
      <li><a href="/cap-cana-golf-villa">Cap Cana Golf Villa</a></li>
      <li><a href="/luxury-golf-villa">Luxury Golf Villas</a></li>
    </ul></div>
    <div class="footer-col"><h4>Book</h4><ul>
      <li><a href="https://www.espadavilla.com/">Villa Espada — Featured Villa</a></li>
      <li><a href="https://www.espadavilla.com/rates.html">Rates & Availability</a></li>
      <li><a href="https://www.espadavilla.com/contact.html">Book Direct</a></li>
    </ul></div>
    <div class="footer-col"><h4>Golf Network</h4><ul>
      <li><a href="https://www.espadavilla.com/">espadavilla.com</a></li>
      <li><a href="https://www.golflasiguanas.com/">golflasiguanas.com</a></li>
      <li><a href="https://www.caribbeangolfcourse.com/">caribbeangolfcourse.com</a></li>
    </ul></div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 GolfVilla.com — The World's Premier Golf Villa Authority</p>
    <p>Featured property: <a href="https://www.espadavilla.com">espadavilla.com</a> · Cap Cana, Dominican Republic</p>
  </div>
</footer>
<script src="/js/main.js"></script>"""


# ─── DESTINATION DATA ─────────────────────────────────────────────────────────
# Each destination: (slug, page_title, h1, meta_desc, overline, hero_p,
#                    section1_h2, section1_body,
#                    section2_h2, section2_body,
#                    section3_h2, section3_body,
#                    cta_p, villa_context)

DESTINATIONS = [
    {
        "slug": "golf-villa-caribbean",
        "title": "Golf Villa Caribbean | Best Private Golf Villa Rentals in the Caribbean",
        "h1": "Golf Villa Caribbean.<br><em>The World's Best.</em>",
        "meta": "The Caribbean's finest private golf villas — ranked and reviewed. Villa Espada at Cap Cana leads the region: Punta Espada Fairway 5, 8 bedrooms, member tee times, private chef.",
        "overline": "Caribbean Golf Villas · Dominican Republic · Cap Cana",
        "hero_p": "The Caribbean is the world's greatest golf villa region. Multiple world-ranked courses, year-round playing conditions, private villas on the fairway, and the combination of a championship golf trip with a genuine Caribbean stay. Villa Espada at Cap Cana sets the standard for the category.",
        "s1_h2": "Why the Caribbean is the World's Top Golf Villa Destination",
        "s1_body": "<p>No other golf region in the world combines championship course quality, year-round playing conditions, luxury private villa infrastructure, and genuine Caribbean lifestyle the way the Dominican Republic's northeast coast does. Specifically: Cap Cana, the private gated resort community that is home to Punta Espada, Las Iguanas, and Villa Espada.</p><p>Punta Espada has been ranked the #1 resort course in Latin America and the Caribbean for nearly two decades. Jack Nicklaus designed it, and five of its holes play directly along the Caribbean Sea. In November 2025, Las Iguanas opened next door — another Nicklaus Signature, with three consecutive oceanside holes and a protected iguana nature reserve. One location. Two world-class courses. One private villa.</p><p>The weather argument is also real: the Dominican Republic's northeast coast plays golf year-round. The peak season (November–April) coincides with the trade winds, which keep the courses firm and fast and the weather ideal. But even the low season (May–October) delivers excellent golf, with quieter courses and more flexible availability.</p>",
        "s2_h2": "Caribbean Golf Villa — What to Look For",
        "s2_body": "<p>Not all Caribbean golf villas are equal. The defining factors that separate a great golf villa from a merely good one: proximity to the course (on the fairway vs. a mile away matters enormously), quality of the included staff (a butler who pre-books tee times before you arrive changes the trip), and the actual course access provided (member rates vs. public booking vs. no preferential access at all).</p><p>Villa Espada scores at the highest level on each criterion. It sits directly on Punta Espada Fairway 5 — walk out the back of the villa onto the course. The villa includes a full-time private chef, personal butler, and housekeeping staff. And your tee times at Punta Espada and Las Iguanas are booked at owner/member-tier rates by the butler before you arrive.</p><p>That combination — on the course, full staff, member tee access — is what defines the world's premier golf villa. In the Caribbean, Villa Espada is the clearest example of the category at its best.</p>",
        "s3_h2": "Planning Your Caribbean Golf Villa Trip",
        "s3_body": "<p>The optimal stay at Villa Espada in Cap Cana is 5–7 nights during peak season (November–April). This allows your group to play Punta Espada twice and Las Iguanas twice, with a rest day in between for pool time, the Cap Cana marina, Punta Cana beach access, or the Cap Cana waterpark. A 7-night stay gives the group time to play Corales or La Cana for a third course option.</p><p>Flights to Punta Cana International Airport (PUJ) operate from numerous North American and European hubs. The villa arranges private airport transfers; the drive from PUJ to Cap Cana is approximately 20 minutes.</p><p>Peak season books out quickly — particularly the Christmas/New Year's and Easter windows. If you're planning a specific window, inquiring 6–12 months in advance is advisable for the best availability.</p>",
        "cta_p": "Villa Espada in Cap Cana is the Caribbean's finest golf villa — and the world's finest by any measure. Member tee times, private chef, butler, two golf carts, 8 bedrooms.",
        "villa_context": "the Caribbean's premier golf villa and the global standard-setter for the category"
    },
    {
        "slug": "golf-villa-dominican-republic",
        "title": "Golf Villa Dominican Republic | Private Golf Villa DR · Cap Cana",
        "h1": "Golf Villa Dominican Republic.<br><em>The Best in the Americas.</em>",
        "meta": "The Dominican Republic's finest golf villas — Cap Cana, Punta Espada, Las Iguanas. Villa Espada on Fairway 5 is the DR's premier golf villa. 8 bedrooms, member tee times, private chef.",
        "overline": "Dominican Republic · Cap Cana · Punta Espada Fairway 5",
        "hero_p": "The Dominican Republic is the Americas' premier golf destination. Five world-ranked courses within 90 minutes of each other — Punta Espada, Las Iguanas, Corales, La Cana, Teeth of the Dog. Villa Espada in Cap Cana sits on Fairway 5 of the best of them.",
        "s1_h2": "The Dominican Republic — Golf Villa Paradise",
        "s1_body": "<p>No country in the Western Hemisphere offers the concentration of world-class golf that the Dominican Republic does. Within a 90-minute radius of Cap Cana, you can access Punta Espada (ranked #1 in Latin America for nearly two decades), Las Iguanas (the new Jack Nicklaus Signature opened November 2025), Corales Golf Club (PGA Tour venue), La Cana (four 9-hole combinations along the Caribbean), and Teeth of the Dog at Casa de Campo (Pete Dye's 1971 masterpiece, often ranked the #1 course in the Caribbean).</p><p>For a private golf villa trip in the DR, the strategic center is Cap Cana. Villa Espada is inside the resort, on Punta Espada Fairway 5, with member access to Punta Espada and Las Iguanas. The butler can arrange day-trip transportation to Corales (15 min), La Cana (15 min), and Casa de Campo (90 min by private chauffeur) for groups wanting to extend their itinerary beyond Cap Cana.</p>",
        "s2_h2": "Dominican Republic Golf Villa Seasons",
        "s2_body": "<p><strong>Peak Season (November–April)</strong> is the trade wind season on the DR's northeast coast. The courses play firmer and faster, the weather is drier, and the atmosphere at Cap Cana is at its most vibrant. This is when international golf groups, corporate retreats, and major events fill the resort. Book 6–12 months in advance for this window.</p><p><strong>Low Season (May–October)</strong> offers more flexible availability, lower rates ($2,500/night vs. $4,500/night peak), and excellent golf. The northeast coast is partially sheltered from the Atlantic hurricane track by the geography of the island. The courses play beautifully, the resort is quieter, and groups who want space and flexibility often prefer this window.</p><p><strong>Holiday Windows (Christmas, New Year's, Easter)</strong> book out the furthest in advance. These require a 7-night minimum and are priced at $6,500/night. If a holiday week is your target, inquire 12+ months ahead.</p>",
        "s3_h2": "5-Course DR Golf Itinerary from Villa Espada",
        "s3_body": "<p><strong>Day 1–2: Punta Espada.</strong> Start with the course outside your back door. Play it twice across the trip — once early in the stay to learn the layout, once near the end when you know the club selection on the ocean holes. The second round is always better.</p><p><strong>Day 3: Las Iguanas.</strong> The new Nicklaus Signature. First timer on this course — the nature reserve, the iguana caves, the par-3 13th. A completely different visual experience from Punta Espada despite sitting next door.</p><p><strong>Day 4: Rest day or optional round.</strong> Pool, marina, Punta Cana beach, Cap Cana waterpark.</p><p><strong>Day 5: Corales or La Cana.</strong> 15 minutes from the villa. Corales is a PGA Tour venue. La Cana gives you four 9-hole combinations along the Caribbean.</p><p><strong>Day 6: Teeth of the Dog (optional).</strong> 90 minutes by private chauffeur to Casa de Campo. Pete Dye's 1971 original — seven holes play directly along the Caribbean Sea. One of the greatest golf days available anywhere in the world.</p>",
        "cta_p": "Villa Espada at Cap Cana is the Dominican Republic's finest golf villa. On Punta Espada Fairway 5, member tee times at two world-class Nicklaus courses, private chef and full staff.",
        "villa_context": "the DR's and the Americas' premier golf villa"
    },
    {
        "slug": "golf-villa-scotland",
        "title": "Golf Villa Scotland | Private Golf Villa Rental · Links Golf Stays",
        "h1": "Golf Villa Scotland.<br><em>Links Golf, Private Estate.</em>",
        "meta": "Private golf villa rentals in Scotland — St Andrews, Turnberry, Carnoustie. And when you want the world's best golf villa on a championship course, Villa Espada at Cap Cana is the benchmark.",
        "overline": "Golf Villa Scotland · Links Golf · Private Estates",
        "hero_p": "Scotland is where golf began. A private estate near St Andrews, Turnberry, or Carnoustie is the classic golf trip. But if you're looking for the world's best golf villa — with member tee times, private chef, full staff, and a course that rivals the great Scottish links — Cap Cana sets the global standard.",
        "s1_h2": "Golf Villas in Scotland — The Links Experience",
        "s1_body": "<p>Scotland's golf travel tradition is built around private house stays near the great links courses. A cottage on the Old Course Road in St Andrews. A country house estate within walking distance of Turnberry. A farmhouse rental near Carnoustie with sea views. This is the traditional Scottish golf trip, and it remains one of the finest travel experiences in the world for serious golfers.</p><p>True golf villas in the modern sense — private residences directly on a championship course, with dedicated staff, member tee access, and full concierge — are less common in Scotland than in the Caribbean. The infrastructure of private luxury villa tourism around the Scottish links is more cottage-rental than staff-included estate. For the fully-staffed golf villa experience, the Dominican Republic is where the market is most developed.</p>",
        "s2_h2": "The Alternative — Cap Cana vs Scotland for a Golf Villa Trip",
        "s2_body": "<p>The Scottish golf trip and the Cap Cana golf villa trip serve different purposes. Scotland is a pilgrimage — the Old Course, Carnoustie, Turnberry, Kingsbarns, the history and the landscape and the wind. If playing the great links courses is the objective, Scotland is irreplaceable.</p><p>Cap Cana offers something different: a private villa directly on a world-ranked course, with full private staff, member tee times at two Nicklaus courses, perfect weather, and a location purpose-built for luxury private group travel. For annual golf trips, bachelor parties, corporate outings, and family vacations where the combination of extraordinary golf and extraordinary private accommodation is the goal, Villa Espada at Cap Cana is the comparison point the world uses.</p><p>Many serious golfers do both in the same year: Scotland for the pilgrimage, Cap Cana for the private villa experience.</p>",
        "s3_h2": "What Makes Cap Cana the World's Premier Golf Villa Destination",
        "s3_body": "<p>Punta Espada — the Jack Nicklaus Signature design ranked #1 in Latin America and the Caribbean — is the centerpiece. Five holes play along the Caribbean Sea. The course is immaculate, tournament-conditioned, and visually unlike anything else in the Americas. In November 2025, Las Iguanas opened next door: another Nicklaus Signature, with three oceanside holes and a protected iguana nature reserve, already drawing comparisons to the great par-3s of Ballybunion and Lahinch.</p><p>Villa Espada sits on Punta Espada Fairway 5 with 8 bedrooms, private chef, butler, two golf carts, and member tee time access to both courses. The combination of on-course private estate accommodation with championship golf access and full private staff is what makes it the global benchmark for the golf villa category — regardless of what Scotland, Ireland, or Portugal offer.</p>",
        "cta_p": "Villa Espada at Cap Cana — the golf villa that Scotland, Ireland, and Portugal get compared to. On Punta Espada Fairway 5. Member tee times. Private chef. Full staff.",
        "villa_context": "the global benchmark that all other golf villa destinations are measured against"
    },
    {
        "slug": "golf-villa-ireland",
        "title": "Golf Villa Ireland | Private Golf Villa Rental · Irish Links Stays",
        "h1": "Golf Villa Ireland.<br><em>Links Golf, Private House.</em>",
        "meta": "Golf villa rentals near Ireland's best links courses — Ballybunion, Royal County Down, Lahinch. And the world's finest staffed golf villa is Villa Espada at Cap Cana, DR.",
        "overline": "Golf Villa Ireland · Ballybunion · Royal County Down · Lahinch",
        "hero_p": "Ireland's links courses are among the world's finest. A private house near Ballybunion, Royal County Down, or Lahinch is a golf trip that belongs on every serious golfer's list. For the fully-staffed golf villa experience with member tee times, private chef, and a course you walk onto from your back door — Cap Cana sets the global standard.",
        "s1_h2": "Golf Villas in Ireland — The Links Tradition",
        "s1_body": "<p>Ireland's golf travel market is built on the same tradition as Scotland — private house rentals near the great links courses. Cottage stays in County Clare near Lahinch and Spanish Point. Farmhouse rentals near Ballybunion with views over the Atlantic. Country houses in County Down within range of Royal County Down and Royal Portrush. This is the Irish golf trip, and for golfers who want links golf at its most authentic, it is extraordinary.</p><p>The challenge with Irish golf villa stays is similar to Scotland: the fully-staffed golf villa concept — with a dedicated private chef, personal butler, member tee time access, and golf carts — is less developed than in the Caribbean. Most Irish golf house rentals are self-catered or have minimal included service. The distinction between a holiday rental near a great course and a true golf villa with full private staff is significant.</p>",
        "s2_h2": "Ireland vs Cap Cana — Golf Villa Comparison",
        "s2_body": "<p>These are not competing options — they are different golf trips with different purposes. An Irish links trip is a pilgrimage: Ballybunion, Lahinch, Waterville, Royal County Down, Portrush. The courses, the landscape, the wind off the Atlantic, the history. If authentic links golf is the objective, Ireland is not comparable to anywhere else.</p><p>A Cap Cana golf villa trip is about something specific: an 8-bedroom private estate directly on a world-ranked Nicklaus course, with a private chef handling every meal, a butler with your tee times pre-booked at member rates, two golf carts in the garage, and the combination of championship golf with a genuinely private luxury estate stay. This is the golf villa concept at its most fully realized, and Villa Espada at Cap Cana is the best example in the world.</p>",
        "s3_h2": "Cap Cana — The Golf Villa Ireland Gets Compared To",
        "s3_body": "<p>Golfers who have been to Ireland and Scotland and are looking for the private villa version of the same passion — championship golf as the anchor of a fully private, fully staffed group stay — find Cap Cana as the answer. Punta Espada and Las Iguanas are legitimate world-class courses that draw direct comparisons to the great oceanside holes of Lahinch, Ballybunion, and Portrush. The difference is the villa infrastructure: Villa Espada gives you what the Irish cottage rental cannot — a private chef cooking three meals a day, a butler booking tee times in advance, and the ability to walk from your infinity pool directly onto Fairway 5.</p>",
        "cta_p": "Villa Espada at Cap Cana — the Caribbean's answer to the Irish links golf trip. On Punta Espada Fairway 5. Private chef. Butler. Member tee times at two world-class courses.",
        "villa_context": "the destination serious golfers add after Ireland and Scotland"
    },
    {
        "slug": "golf-villa-portugal",
        "title": "Golf Villa Portugal | Private Golf Villa Algarve · GolfVilla.com",
        "h1": "Golf Villa Portugal.<br><em>Algarve & Beyond.</em>",
        "meta": "Golf villa rentals in Portugal's Algarve — Vale do Lobo, Quinta do Lago, Vilamoura. And the world's finest staffed golf villa is Villa Espada at Cap Cana, Dominican Republic.",
        "overline": "Golf Villa Portugal · Algarve · Vale do Lobo · Quinta do Lago",
        "hero_p": "Portugal's Algarve is Europe's most popular golf destination. Year-round sunshine, world-ranked resort courses, and a well-developed private villa market. For the fully-staffed golf villa experience at its absolute finest — on the fairway, member tee times, private chef, full staff — Cap Cana in the Dominican Republic is where the global bar is set.",
        "s1_h2": "Golf Villas in Portugal — The Algarve Option",
        "s1_body": "<p>Portugal's Algarve coast offers Europe's strongest golf villa market. The combination of year-round playing weather, multiple world-ranked resort courses (Vale do Lobo, Quinta do Lago, Vilamoura, Monte Rei), and a mature private villa rental infrastructure makes it the European golfer's natural destination. Private villas in golf resorts like Vale do Lobo Royal or Quinta do Lago are genuinely on or directly adjacent to course holes, with varying levels of included service.</p><p>The quality range in Algarve golf villas is wide. The best properties — typically in the premium residential areas of Vale do Lobo Royal, Quinta do Lago, or Monte Rei — can offer genuine on-course positioning, private pools, and catering services arranged through the resort. The challenge is finding the combination of on-course villa, full private staff, and member-tier tee access in one package.</p>",
        "s2_h2": "Portugal vs Cap Cana for a Golf Villa Trip",
        "s2_body": "<p>Portugal has obvious advantages for European golfers: a short flight from the UK and Western Europe, no jet lag, familiar culture, excellent food and wine, and courses that are genuinely world-class. The Algarve golf villa trip makes enormous logistical sense for a group flying from London, Amsterdam, or Madrid.</p><p>For North American and international groups — where the flight to Lisbon and the flight to Punta Cana are broadly comparable in length — Cap Cana offers a compelling alternative. The key differentiator is the villa concept at Villa Espada: fully staffed with a dedicated private chef and personal butler, positioned on Punta Espada Fairway 5, with member tee time access to two world-ranked Nicklaus courses. The all-inclusive private estate model is more fully realized at Villa Espada than at comparable Algarve properties.</p>",
        "s3_h2": "Why the World's Serious Golf Travelers Choose Cap Cana",
        "s3_body": "<p>Golfers who have played Vale do Lobo, Quinta do Lago, and Monte Rei and who are looking for the private villa concept taken to its maximum expression find Villa Espada as the answer. Punta Espada and Las Iguanas are genuine world-ranked courses with ocean holes comparable to the best in Europe. The villa is on the fairway, fully staffed, and designed from the ground up for groups who want the golf trip and the private estate stay to be inseparable — not just geographically proximate but operationally integrated, with the same staff managing both the villa and the tee sheet.</p>",
        "cta_p": "Villa Espada at Cap Cana — the private golf villa that Portugal gets compared to. On Punta Espada Fairway 5. Private chef, butler, member tee times at two Nicklaus courses.",
        "villa_context": "the destination that sets the global standard for fully-staffed golf villa travel"
    },
    {
        "slug": "golf-villa-spain",
        "title": "Golf Villa Spain | Private Golf Villa Costa del Sol · GolfVilla.com",
        "h1": "Golf Villa Spain.<br><em>Costa del Sol & Sotogrande.</em>",
        "meta": "Golf villa rentals in Spain — Costa del Sol, Marbella, Sotogrande. Valderrama, Real Club Sotogrande. And the world's finest staffed golf villa: Villa Espada at Cap Cana, DR.",
        "overline": "Golf Villa Spain · Costa del Sol · Marbella · Sotogrande",
        "hero_p": "Spain's Costa del Sol is Europe's golf capital — Valderrama, Real Club Sotogrande, La Reserva, Las Brisas, more than 70 courses within an hour of Marbella. Private golf villas exist throughout the region. For the fully-staffed, on-the-fairway golf villa experience at its global best, Villa Espada at Cap Cana is the benchmark.",
        "s1_h2": "Golf Villas in Spain — Costa del Sol and Sotogrande",
        "s1_body": "<p>Spain's southern coast has the highest concentration of golf courses in Europe, and a well-developed private villa rental market to match. Sotogrande — the private estate community near Gibraltar — is home to Valderrama (site of the 1997 Ryder Cup), Real Club Sotogrande, and La Reserva, with numerous private villas within the estate boundaries. Marbella, Puerto Banus, and the Golden Mile offer private villa stays near Las Brisas, Aloha, and Los Naranjos.</p><p>Sotogrande's private villa market in particular shares some DNA with the golf villa concept: gated community, private properties, access to world-class courses. The difference is infrastructure: most Sotogrande villa rentals are self-catered or minimally staffed, and tee time access is managed through public booking rather than owner/member-tier rates.</p>",
        "s2_h2": "Spain vs Cap Cana — Golf Villa Comparison",
        "s2_body": "<p>Spain and Cap Cana offer different versions of the golf villa trip. Spain is accessible from Europe, has world-class courses including Valderrama, and a warm Mediterranean climate. For European golfers, it is the natural first golf villa destination.</p><p>Cap Cana's Villa Espada offers the concept taken further: a fully staffed private estate on a world-ranked course, with a dedicated private chef preparing every meal, a personal butler managing the tee sheet at member rates, two golf carts, private airport transfers, and the combination of Caribbean lifestyle with championship golf. For groups who want the maximum expression of the golf villa concept — whether from North America, Europe, or internationally — Villa Espada is the reference point.</p>",
        "s3_h2": "Valderrama and Punta Espada — The Two Extremes",
        "s3_body": "<p>Valderrama and Punta Espada represent two poles of championship golf design excellence — Valderrama the tight, wooded, precision-demanding parkland that humbled the world's best players at the Ryder Cup; Punta Espada the open, drama-filled oceanside Nicklaus design that rewards strategic play and punishes overconfidence on the Caribbean holes. Both are legitimately world-class. Both are unforgettable. Both deserve to be on a serious golfer's itinerary.</p><p>The private villa experience around each is very different. Sotogrande has villas within the community. Cap Cana has Villa Espada — directly on Fairway 5 of Punta Espada, with full private staff and member access to both Punta Espada and Las Iguanas. The gap in the private staff and tee access experience is significant.</p>",
        "cta_p": "Villa Espada at Cap Cana — the golf villa that Sotogrande and the Costa del Sol get measured against. On Punta Espada Fairway 5. Private chef, butler, member tee times.",
        "villa_context": "the global benchmark for the fully-staffed, on-course golf villa experience"
    },
    {
        "slug": "golf-villa-punta-cana",
        "title": "Golf Villa Punta Cana | Private Golf Villa Rental · Cap Cana DR",
        "h1": "Golf Villa Punta Cana.<br><em>The Best Address in the Region.</em>",
        "meta": "Golf villa rental in the Punta Cana region — Villa Espada at Cap Cana on Punta Espada Fairway 5. The finest golf villa in the Punta Cana area. Member tee times, private chef, 8 bedrooms.",
        "overline": "Punta Cana Region · Cap Cana · Punta Espada Fairway 5",
        "hero_p": "The Punta Cana region of the Dominican Republic is home to the Caribbean's greatest concentration of championship golf. Punta Espada, Las Iguanas, Corales, La Cana — all within 20 minutes of each other. Villa Espada at Cap Cana is the region's finest private golf villa, sitting directly on Punta Espada Fairway 5.",
        "s1_h2": "Punta Cana Golf — The Region's Championship Courses",
        "s1_body": "<p>The Punta Cana region encompasses several distinct resort communities within a short drive of each other — Punta Cana Resort, Cap Cana, and the broader Cap Cana Golf Club complex. The golf within the region includes Punta Espada (Jack Nicklaus Signature, #1 in Latin America), Las Iguanas (Jack Nicklaus Signature, opened November 2025), Corales Golf Club (PGA Tour host), and La Cana Golf Club (four 9-hole combinations along the Caribbean).</p><p>Cap Cana — the private gated resort community adjacent to but distinct from Punta Cana Resort — is home to Punta Espada and Las Iguanas. It is the premium address in the Punta Cana region, with its own marina, private beach, waterparks, and residential estates. Villa Espada is inside Cap Cana, on Punta Espada Fairway 5.</p>",
        "s2_h2": "The Best Golf Villa in the Punta Cana Area",
        "s2_body": "<p>Villa Espada is the best golf villa in the Punta Cana region by any measure. It sits on Fairway 5 of Punta Espada — the top-ranked course in the region and in all of Latin America. It includes 8 bedrooms, a private chef, personal butler, two six-person golf carts, and member tee time access at Punta Espada and Las Iguanas. Private airport transfers from Punta Cana International Airport (PUJ) are included; the drive from PUJ to the villa is approximately 20 minutes.</p><p>For groups searching for a golf villa in the Punta Cana area — whether the primary search term is 'Punta Cana golf villa,' 'Cap Cana golf villa,' or 'Dominican Republic golf villa' — Villa Espada is the answer. The address is Cap Cana; the destination is Punta Espada golf course; the experience is the best private golf villa in the Caribbean.</p>",
        "s3_h2": "Getting to Your Punta Cana Golf Villa",
        "s3_body": "<p>Punta Cana International Airport (PUJ) is one of the busiest international airports in the Caribbean, with direct nonstop service from dozens of North American cities including New York, Miami, Boston, Chicago, Atlanta, Dallas, Toronto, and Montreal, plus connections from Europe through Madrid, London, and Amsterdam.</p><p>Once you land at PUJ, Villa Espada's concierge team arranges private vehicle transfer directly to the villa — a 20-minute drive along a well-maintained highway into Cap Cana. By the time your group reaches the villa, the butler has confirmed your tee times and the chef is preparing the first meal. The transition from airport to fairway is under two hours.</p>",
        "cta_p": "The best golf villa in the Punta Cana region. Villa Espada at Cap Cana — Punta Espada Fairway 5. Member tee times, private chef, 8 bedrooms, full staff.",
        "villa_context": "the finest golf villa in the Punta Cana region and the best in the Caribbean"
    },
    {
        "slug": "golf-villa-annual-golf-trip",
        "title": "Golf Villa Annual Golf Trip | Private Golf Villa for Groups · GolfVilla.com",
        "h1": "The Annual Golf Trip.<br><em>Done Properly.</em>",
        "meta": "Planning your annual golf trip? A private golf villa at Cap Cana is the upgrade your group has been talking about. Villa Espada — Punta Espada Fairway 5, private chef, member tee times, 8 bedrooms.",
        "overline": "Annual Golf Trip · Golf Villa · Cap Cana · Dominican Republic",
        "hero_p": "Your annual golf group has been to Scottsdale. You've done Myrtle Beach twice. Someone's been to Ireland and keeps talking about it. The upgrade your group actually needs is a private villa on a world-ranked course with a chef, a butler, member tee times, and no logistics to manage. That's Villa Espada at Cap Cana.",
        "s1_h2": "Why a Golf Villa Changes the Annual Trip",
        "s1_body": "<p>The annual golf trip formula — everyone books a hotel room, everyone figures out their own dinners, someone manages the tee sheet, the logistics of moving 8–16 people between hotel, restaurant, and golf course consume energy that should be going into the game — is a familiar friction point. A private golf villa eliminates all of it.</p><p>One all-inclusive rate covers accommodation, chef-prepared meals every day, a butler who handles every tee time and logistical detail, two golf carts, and the ability for the group to stay together in a private space that belongs to you for the week. No hotel lobby. No shared amenities with other guests. No coordinating who's going where for dinner. The chef cooks. The butler books. The group golfs.</p><p>For annual golf groups who have been doing the same trip for years and are ready for the version that actually lands as extraordinary — Villa Espada at Cap Cana is that trip.</p>",
        "s2_h2": "What Your Annual Golf Group Gets at Villa Espada",
        "s2_body": "<p>8 bedrooms sleeping up to 22 guests. Infinity pool overlooking Punta Espada Fairway 5. Multiple outdoor terraces and dining spaces. Private chef handling breakfast, lunch, and dinner every day. Personal butler with tee times at Punta Espada and Las Iguanas pre-booked at member/owner-tier rates before you arrive. Two six-person golf carts, fueled. Private transfers from PUJ airport. Housekeeping throughout the stay.</p><p>For a group of 8 splitting the cost in peak season ($4,500/night), the per-person nightly rate is approximately $562. Fully all-inclusive for accommodation, all meals, and golf access infrastructure. Compare that to 8 hotel rooms, 8 restaurant dinners each night, individual transfers, and public green fee rates at the same courses. The villa economy is almost always more favorable once you do the math — and the experience isn't comparable.</p>",
        "s3_h2": "Planning the Annual Golf Trip to Cap Cana",
        "s3_body": "<p>The ideal duration is 5–7 nights. A 5-night stay allows two rounds each at Punta Espada and Las Iguanas, with one evening of arrival and one departure morning bookending the trip. A 7-night stay gives the group the option to add Corales (15 min from the villa), La Cana (15 min), or Teeth of the Dog at Casa de Campo (90-min chauffeur day trip) for a third course variety.</p><p>Peak season (November–April) is the most sought-after window. The trade winds keep the courses firm, fast, and dry. Book 6–12 months in advance for the best availability, particularly for groups of 12+ who need multiple bedrooms to be confirmed together.</p>",
        "cta_p": "Villa Espada at Cap Cana — the annual golf trip upgrade your group has been looking for. Member tee times, private chef, full staff, 8 bedrooms on Punta Espada Fairway 5.",
        "villa_context": "the annual golf trip that golfers who have been everywhere else talk about for years afterward"
    },
    {
        "slug": "golf-bachelor-party-villa",
        "title": "Golf Bachelor Party Villa | Private Golf Villa Bachelor Party · GolfVilla.com",
        "h1": "Golf Bachelor Party Villa.<br><em>The One They'll Remember.</em>",
        "meta": "Planning a golf bachelor party villa trip? Villa Espada at Cap Cana — 8 bedrooms for up to 22 guests, private chef, two world-class Nicklaus courses, private pool. The world's best golf bachelor party destination.",
        "overline": "Golf Bachelor Party · Villa Espada · Cap Cana · Dominican Republic",
        "hero_p": "Up to 22 guys. Two Jack Nicklaus courses. A private chef cooking every meal. A pool overlooking the fairway. A butler who books tee times before anyone lands. There is no better golf bachelor party venue in the world. Villa Espada at Cap Cana is it.",
        "s1_h2": "Why Villa Espada is the World's Best Golf Bachelor Party Venue",
        "s1_body": "<p>A golf bachelor party requires several things to succeed: enough bedrooms for a large group (Villa Espada sleeps up to 22), world-class courses no one has played before, private space for the group to do what they want without hotel guests around, a chef so no one is coordinating dinner reservations every night, and a location that feels genuinely extraordinary rather than a city everyone has already been to.</p><p>Villa Espada at Cap Cana delivers on every criterion. Eight bedrooms. An infinity pool on Punta Espada Fairway 5. A private chef. Two Jack Nicklaus Signature courses — Punta Espada (#1 in Latin America for nearly 20 years) and Las Iguanas (opened November 2025) — with member tee times included. Private airport transfers. Housekeeping. A butler who runs the tee sheet and handles any request your group has.</p><p>The combination of having the villa entirely to yourselves — no hotel lobby, no other guests' schedules, no noise complaints — with championship golf and a private chef creates the conditions for the golf bachelor party trip that the group talks about for the rest of their lives.</p>",
        "s2_h2": "Planning Your Golf Bachelor Party at Villa Espada",
        "s2_body": "<p><strong>Group size:</strong> Villa Espada works best for groups of 8–22. For groups larger than 22, the villa team can recommend additional accommodation options within Cap Cana that allow a larger group to stay nearby and share the villa's tee time and concierge access.</p><p><strong>Duration:</strong> 4–5 nights is the sweet spot for bachelor party groups. Enough time for two rounds each at Punta Espada and Las Iguanas, plus pool time, meals together, and evening activities. The villa chef can organize a special welcome dinner and a farewell evening with as much or as little ceremony as the group wants.</p><p><strong>Booking timeline:</strong> Golf bachelor parties at Villa Espada tend to book 6–12 months in advance, particularly for peak season (November–April) and holiday windows. If you have a specific date or week in mind, inquiring early gives you the best shot at your preferred window.</p><p><strong>What the butler handles:</strong> All tee times at member/owner rates, ground transportation within Cap Cana and to/from the airport, restaurant reservations for nights the group wants to eat out, excursions (marina, beach, waterpark), and any special requests for the stay.</p>",
        "s3_h2": "Golf Bachelor Party Costs at Villa Espada",
        "s3_body": "<p>In peak season (November–April), the villa rate is $4,500/night with a 5-night minimum — a total of $22,500 for the villa itself, inclusive of private chef, butler, golf carts, housekeeping, and airport transfers. Split across 10 guys, that's $2,250 each for the entire stay (accommodation + meals + logistics). Add flights, green fees at member rates, and incidentals, and a 5-night villa bachelor party for 10 in peak season typically totals $3,000–$4,500 per person all-in, depending on flights.</p><p>That compares very favorably to 10 hotel rooms in Las Vegas, Scottsdale, or any major US golf destination once you add resort fees, restaurant dinners, green fees at public rates, and group transportation.</p>",
        "cta_p": "Book the world's best golf bachelor party villa. Villa Espada at Cap Cana — Punta Espada Fairway 5, private chef, member tee times, up to 22 guests.",
        "villa_context": "the world's best golf bachelor party venue by every measure"
    },
    {
        "slug": "corporate-golf-villa-retreat",
        "title": "Corporate Golf Villa Retreat | Private Golf Villa Corporate Event · GolfVilla.com",
        "h1": "Corporate Golf Villa Retreat.<br><em>Impress the Clients That Matter.</em>",
        "meta": "Corporate golf villa retreats at Villa Espada, Cap Cana. Private villa on Punta Espada Fairway 5, private chef, member tee times at two world-class courses. The corporate golf retreat that impresses clients who travel constantly.",
        "overline": "Corporate Golf Retreat · Villa Espada · Cap Cana · Dominican Republic",
        "hero_p": "Clients who have seen everything are hard to impress. A private villa on a Jack Nicklaus course in the Dominican Republic, with a private chef handling every meal and a butler pre-booking tee times at courses they've never played — that registers. Villa Espada at Cap Cana is the corporate golf retreat that lands differently.",
        "s1_h2": "Why a Private Golf Villa is the Best Corporate Retreat Format",
        "s1_body": "<p>The corporate golf trip format — hotel block booking, group dinner reservation, tee times coordinated through the resort, everything happening in a shared space with other hotel guests — is familiar and functional. A private villa corporate retreat is a different category of experience, and it creates different impressions.</p><p>When your clients arrive at a private 10,000+ sq ft estate on Punta Espada Fairway 5 and find the chef has breakfast ready, the butler has confirmed their tee times at member rates, and the entire villa is exclusively for your group — the message is clear. This wasn't a package. This was thought through. The relationship building that happens in a private villa, over chef-prepared dinners on a Caribbean terrace, with the day built around golf at a course everyone will talk about — is more effective than any hotel ballroom.</p>",
        "s2_h2": "Villa Espada for Corporate Golf Retreats",
        "s2_body": "<p>Villa Espada is well-suited for corporate groups of 6–16. The villa's 8 bedrooms sleep up to 22, but corporate groups in the 6–10 range tend to use 4–6 bedrooms and have more living space per person — which works well for the combination of downtime, private conversations, and group meals that define a successful corporate retreat.</p><p>The butler and concierge team can organize: pre-arrival tee time booking at Punta Espada and Las Iguanas at member/owner rates; welcome dinner with any dietary accommodations handled; roundtable dinner for business discussions on the villa's private terrace; excursion options (marina, beach, Cap Cana waterpark) for non-golf guests or off-golf afternoons; airport transfers for all guests timed to individual arrival schedules.</p><p>The private chef prepares three meals daily — briefing breakfast, post-round lunch, and evening dinner — at a standard consistent with the villa's luxury positioning. Any welcome gifts, custom menus, or branded collateral can be arranged through the concierge team with sufficient advance notice.</p>",
        "s3_h2": "Corporate Golf Retreat ROI — Private Villa vs Resort Hotel",
        "s3_body": "<p>The ROI argument for a private villa corporate retreat over a resort hotel block is primarily experiential — and the best measurement is what clients say to each other after the trip. In our experience, clients who experience Villa Espada tend to tell the story: the villa on the fairway, the chef who knew how they took their coffee on day two, the tee time at Punta Espada at sunrise with no other groups on the course. That narrative retelling — to spouses, to colleagues, at cocktail parties — is the outcome a corporate relationship-building event is trying to create.</p><p>From a pure cost perspective, 8 executives at $4,500/night villa rate for 4 nights = $18,000. Vs 8 luxury hotel rooms at $800/night for 4 nights = $25,600, plus 4 restaurant dinners for 8 = $4,800, plus 8 individual transfers = $1,200. The villa, at $2,250/person for 4 nights inclusive, frequently comes in below the hotel equivalent once all costs are included.</p>",
        "cta_p": "Villa Espada at Cap Cana — the corporate golf retreat that impresses clients who have seen everything. Private villa on Punta Espada Fairway 5, private chef, member tee times.",
        "villa_context": "the corporate golf retreat that changes the conversation with clients who travel constantly"
    },
    {
        "slug": "golf-villa-family-vacation",
        "title": "Golf Villa Family Vacation | Golf Family Trip Villa · GolfVilla.com",
        "h1": "Golf Villa Family Vacation.<br><em>Something for Everyone.</em>",
        "meta": "A private golf villa family vacation at Cap Cana. Villa Espada — 8 bedrooms for up to 22, private chef, two world-class golf courses, Cap Cana Waterpark, private pool. Golf for the golfers. Everything for the family.",
        "overline": "Golf Villa Family Vacation · Villa Espada · Cap Cana · Dominican Republic",
        "hero_p": "The challenge of the family golf vacation: the golfers want to play great courses, and the non-golfers want a great vacation. Villa Espada at Cap Cana solves both. Championship golf on two Nicklaus courses for the golfers. Private pool, private chef, Cap Cana Waterpark, marina, and beaches for everyone else.",
        "s1_h2": "Golf Villa Family Vacation — Why Cap Cana Works",
        "s1_body": "<p>A private golf villa family vacation requires the same thing any family trip requires: something genuinely compelling for every person in the group, regardless of whether they golf. The challenge of most golf resort destinations is that the non-golf programming is secondary — a sop to the partners and kids rather than a genuine reason to travel.</p><p>Cap Cana is different. Inside the Cap Cana resort, non-golfing family members have access to the Cap Cana Waterpark (one of the largest in the Caribbean), multiple private beaches, the 800-slip marina with fishing, snorkeling, and boat excursions, Jaguar Explorer ecological adventures through Cap Cana's jungle terrain, resort restaurants, and the private pool and terrace of Villa Espada itself.</p><p>For the golfers: two world-ranked Jack Nicklaus Signature courses with member tee time access. For everyone else: a private luxury estate with a chef cooking every meal and a butler managing any request. Both groups get a trip they would not have had otherwise.</p>",
        "s2_h2": "Villa Espada for Multi-Generational Family Golf Trips",
        "s2_body": "<p>Multi-generational family golf trips — two or three generations, mixed golfers and non-golfers, varying activity levels — are one of Villa Espada's strongest use cases. The villa's 8 bedrooms accommodate family groups of varying sizes; the open-plan living and dining areas create natural gathering spaces for large family meals; the private pool and terrace give everyone a shared outdoor space that doesn't require coordination with other guests.</p><p>The private chef is particularly valuable for family groups with varying dietary needs, preferences, and meal schedules. Breakfast can be served over a two-hour window to accommodate different wake-up times. Kids' menus, dietary accommodations, special occasion cooking for a birthday or anniversary dinner during the stay — all handled by the chef without the family needing to coordinate at a restaurant.</p>",
        "s3_h2": "Family Golf Vacation at Villa Espada — What to Expect",
        "s3_body": "<p>A typical day at Villa Espada for a multi-generational family group: the golfers are out by 7:30am with tee times at Punta Espada or Las Iguanas already confirmed. The non-golfers have breakfast at their own pace, then the choice of waterpark, beach excursion, marina, or the villa pool with the chef available for lunch whenever they return. The golfers are back mid-afternoon, the pool fills up, and the chef starts dinner as the group reconvenes on the terrace with the fairway view turning gold in the late afternoon light.</p><p>That rhythm — private space, professional staff managing every detail, extraordinary activities for every person in the family — is what the private golf villa delivers that no hotel, however good, can replicate.</p>",
        "cta_p": "Villa Espada at Cap Cana — the family golf vacation where the golfers play two Nicklaus courses and the non-golfers have the Caribbean's finest resort at their door. Private chef, full staff, 8 bedrooms.",
        "villa_context": "the family golf vacation that works for every member of the family"
    },
    {
        "slug": "golf-villa-anniversary",
        "title": "Golf Villa Anniversary & Honeymoon | Romantic Golf Villa · GolfVilla.com",
        "h1": "Golf Villa Anniversary.<br><em>Romance on the Fairway.</em>",
        "meta": "A private golf villa anniversary or honeymoon at Cap Cana. Villa Espada — private pool, private chef, sunset tee times on Punta Espada, butler-arranged romantic dinners. The golf romantic getaway.",
        "overline": "Golf Villa Anniversary · Romantic Golf Trip · Cap Cana · Dominican Republic",
        "hero_p": "A private villa overlooking a Caribbean golf course, a chef who handles every meal, a butler who arranges the sunset tee time and the private terrace dinner. The romantic golf trip — for anniversaries, honeymoons, or any milestone — done properly. Villa Espada at Cap Cana.",
        "s1_h2": "The Romantic Golf Villa — Why It Works",
        "s1_body": "<p>The romantic golf trip has a fundamental challenge: one partner is there for the golf, and the other is there for the experience. In a hotel setting, the golf partner disappears for 5 hours twice a day, and the non-golfing partner is managing their own time around hotel amenities. In a private villa setting, the dynamic is entirely different.</p><p>A private chef cooking breakfast, lunch, and dinner means neither partner has to manage meals or negotiate restaurants. The butler handling tee times and concierge services means the golf partner isn't spending evenings on the phone with the pro shop. The private pool and terrace give the couple a private outdoor space — not a shared resort pool. The villa is entirely theirs. The week belongs to them.</p><p>For couples where one golfs seriously and the other enjoys a luxury Caribbean stay, Villa Espada offers the perfect combination: one of the world's great golf courses at the back door, and a genuinely private luxury estate that the non-golfing partner has no reason to want to leave.</p>",
        "s2_h2": "Anniversary and Honeymoon at Villa Espada",
        "s2_body": "<p>The villa team can arrange special touches for anniversaries, honeymoons, and milestone trips: welcome champagne and floral arrangement on arrival; private terrace dinner on a special evening, with the chef preparing a custom menu; sunset tee time at Punta Espada arranged by the butler; private boat excursion through the Cap Cana marina to a secluded beach; spa appointments at the Cap Cana resort spa.</p><p>For couples traveling alone (using 1–2 bedrooms of the villa's 8), Villa Espada offers a level of privacy and personal service that is rare even in the world's finest hotels. The staff-to-guest ratio when a couple occupies the full villa is extraordinary, and the chef's attention to personalized meals — knowing your dietary preferences, your preferred breakfast timing, your favorite cuisine — creates an experience that a hotel kitchen cannot replicate.</p>",
        "s3_h2": "Planning a Golf Villa Anniversary Trip",
        "s3_body": "<p>For couples, a 4–5 night stay is the ideal duration. Longer stays occasionally feel too long without more guests to fill the villa; 4–5 nights gives the golfing partner enough rounds (2–3 at Punta Espada and Las Iguanas) while giving the couple enough shared time at the villa for the experience to feel like a genuine vacation together rather than a golf trip with a companion.</p><p>Peak season (November–April) offers the best weather and the most vibrant Cap Cana atmosphere. Low season (May–October) is quieter, with more intimate access to the courses and resort facilities — which can suit couples who prefer fewer crowds. Both windows work well for a romantic anniversary trip.</p>",
        "cta_p": "Villa Espada at Cap Cana — the romantic golf villa for anniversaries, honeymoons, and milestone trips. Private chef, butler, sunset tee times on Punta Espada, private terrace dinner.",
        "villa_context": "the most romantic golf villa destination in the world"
    },
    {
        "slug": "international-golf-villa-trip",
        "title": "International Golf Villa Trip | Private Golf Villa Abroad · GolfVilla.com",
        "h1": "International Golf Villa Trip.<br><em>The World-Class Version.</em>",
        "meta": "Planning an international golf villa trip? Villa Espada at Cap Cana is the world's finest — Punta Espada Fairway 5, 8 bedrooms, member tee times, private chef. The international golf trip done at the highest level.",
        "overline": "International Golf Villa Trip · Cap Cana · Dominican Republic",
        "hero_p": "An international golf villa trip is a different category of travel from a domestic golf weekend. A private villa on a world-ranked course, with full private staff and member tee time access, in a location that exists nowhere in the domestic market. Villa Espada at Cap Cana is the world's finest example of what that trip can be.",
        "s1_h2": "Why Go International for Your Golf Villa Trip",
        "s1_body": "<p>The domestic golf trip — Scottsdale, Pebble Beach, Bandon Dunes, Kiawah, Pinehurst — offers world-class golf in an excellent package. What it cannot offer is a private villa with a personal chef on the fairway of a Nicklaus Signature course ranked above Pebble Beach and Augusta National in the 'best resort course' category, with member tee access and full private staff, in a location with Caribbean weather and a 20-minute airport transfer.</p><p>That combination — the course, the villa, the staff, the weather, the airport accessibility — exists in the Dominican Republic and almost nowhere in the domestic US market. Cap Cana is within 4–8 hours of most major US cities by air. The transition from daily life to a private villa on a world-ranked Caribbean course happens faster than a flight to Scotland.</p>",
        "s2_h2": "What Makes the Cap Cana International Trip Exceptional",
        "s2_body": "<p>Punta Espada has been ranked the #1 resort course in Latin America and the Caribbean for nearly two decades. That ranking is not promotional — it reflects consistent performance in Golf Digest, Golf Magazine, and the major international ranking publications. Five holes along the Caribbean Sea. Jack Nicklaus Signature design. Tournament-conditioned fairways and greens. A course that serious golfers who have played Augusta, Pebble Beach, and the Old Course come back from and say it belongs in the conversation.</p><p>The international trip adds one more dimension: novelty. If your golf group has been to every major US destination, Cap Cana is genuinely new — the courses, the destination, the Caribbean setting, the villa-on-the-fairway concept taken to its maximum expression. The combination of a trip that feels like a true international adventure with the logistical ease of a 5-hour direct flight from the US East Coast is rare.</p>",
        "s3_h2": "Logistics — International Golf Villa Trip to Cap Cana",
        "s3_body": "<p>Punta Cana International Airport (PUJ) has direct nonstop service from New York, Miami, Boston, Chicago, Atlanta, Dallas, Toronto, and many other major cities. No connecting flights required for most North American travelers. EU/UK travelers connect through Madrid, London, or Amsterdam. The villa concierge coordinates all airport-to-villa transfers for individual arrival schedules.</p><p>Customs and entry to the Dominican Republic is straightforward for US, Canadian, and EU passport holders — standard tourist entry, no visa required. The villa concierge can brief the group on what to expect on arrival and arrange any local requirements in advance.</p>",
        "cta_p": "Villa Espada at Cap Cana — the international golf villa trip that exists at the highest level. On Punta Espada Fairway 5. Member tee times, private chef, 8 bedrooms, full staff.",
        "villa_context": "the international golf villa trip that serious golfers plan for years"
    },
]


# ─── PAGE GENERATOR ───────────────────────────────────────────────────────────

def make_destination_page(d):
    title = d["title"]
    h1 = d["h1"]
    meta = d["meta"]
    overline = d["overline"]
    hero_p = d["hero_p"]
    s1_h2 = d["s1_h2"]
    s1_body = d["s1_body"]
    s2_h2 = d["s2_h2"]
    s2_body = d["s2_body"]
    s3_h2 = d["s3_h2"]
    s3_body = d["s3_body"]
    cta_p = d["cta_p"]
    canonical = f"https://www.golfvilla.com/SEO-Files/{d['slug']}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
{NAV}

<div class="breadcrumb"><ol>
  <li><a href="/">GolfVilla.com</a></li>
  <li><a href="/golf-villa-rental">Golf Villa Rentals</a></li>
  <li>{h1.replace('<br>', ' ').replace('<em>', '').replace('</em>', '').replace('.', '')}</li>
</ol></div>

<section class="page-hero">
  <div class="page-hero-content">
    <span class="overline">{overline}</span>
    <h1>{h1}</h1>
    <p>{hero_p}</p>
  </div>
</section>

<div class="article-body">
  <div class="container">
    <main class="article-main">
      <div class="article-section fade-up">
        <h2>{s1_h2}</h2>
        <div class="gold-divider"></div>
        {s1_body}
      </div>
      <div class="article-section fade-up">
        <h2>{s2_h2}</h2>
        <div class="gold-divider"></div>
        {s2_body}
      </div>
      <div class="article-section fade-up">
        <h2>{s3_h2}</h2>
        <div class="gold-divider"></div>
        {s3_body}
      </div>
    </main>

    <aside class="article-sidebar">
      <div class="sidebar-cta sidebar-card">
        <h4>Book Villa Espada</h4>
        <p>The world's finest golf villa. Fairway 5 · Punta Espada · Cap Cana. Member tee times, private chef, full staff.</p>
        <a href="https://www.espadavilla.com" class="btn btn-gold" style="width:100%;justify-content:center;margin-top:12px;">View Villa Espada →</a>
        <a href="https://www.espadavilla.com/contact.html" class="btn btn-navy" style="width:100%;justify-content:center;margin-top:8px;">Check Availability</a>
      </div>
      <div class="sidebar-card">
        <h4>Quick Facts · Villa Espada</h4>
        <ul>
          <li>8 Bedrooms · Up to 22 Guests</li>
          <li>On Punta Espada Fairway 5</li>
          <li>Member tee times — 2 courses</li>
          <li>Private chef + butler</li>
          <li>Two golf carts included</li>
          <li>20 min from PUJ airport</li>
          <li>From $2,500/night</li>
        </ul>
      </div>
      <div class="sidebar-card">
        <h4>Golf Network</h4>
        <ul>
          <li><a href="/cap-cana-golf-villa">Cap Cana Golf Villa Guide</a></li>
          <li><a href="/caribbean-golf-villa">Caribbean Golf Villas</a></li>
          <li><a href="https://www.golflasiguanas.com">Las Iguanas Course Guide</a></li>
          <li><a href="https://www.caribbeangolfcourse.com">Caribbean Golf Courses</a></li>
        </ul>
      </div>
    </aside>
  </div>
</div>

<div class="cta-band cta-band-dark">
  <div class="container">
    <h2 style="color:var(--white);">Book Villa Espada</h2>
    <p style="color:rgba(255,255,255,0.7);">{cta_p}</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:40px;">
      <a href="https://www.espadavilla.com" class="btn btn-gold">Book Villa Espada →</a>
      <a href="https://www.espadavilla.com/contact.html" class="btn btn-outline">Check Availability</a>
    </div>
  </div>
</div>

<section class="related-section">
  <div class="container">
    <div class="section-header fade-up"><span class="overline">Keep Exploring</span><h2>More <em>Golf Villa</em> Guides</h2><div class="gold-divider"></div></div>
    <div class="related-grid">
      <div class="related-card fade-up"><span class="overline">Cap Cana</span><h4><a href="/cap-cana-golf-villa">Cap Cana Golf Villa — Full Guide</a></h4><p>The world's finest golf villa destination — two Nicklaus courses, private villa, full staff.</p></div>
      <div class="related-card fade-up"><span class="overline">Caribbean</span><h4><a href="/caribbean-golf-villa">Caribbean Golf Villa Guide</a></h4><p>The best private golf villa destinations across the Caribbean.</p></div>
      <div class="related-card fade-up"><span class="overline">Featured Villa</span><h4><a href="https://www.espadavilla.com">Villa Espada · Book Now</a></h4><p>The world's premier golf villa. Direct booking at espadavilla.com.</p></div>
    </div>
  </div>
</section>

{FOOTER}
</body>
</html>"""


# ─── GENERATE ─────────────────────────────────────────────────────────────────

count = 0
for dest in DESTINATIONS:
    html = make_destination_page(dest)
    path = os.path.join(OUTPUT_DIR, f"{dest['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    count += 1

print(f"✅ Generated {count} destination pages → SEO-Files/")
