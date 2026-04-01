# GolfVilla.com — Geo Page Generator
# Generates 200+ geo-targeted pages: "Golf Villa [City]" + "Golf Villa Rental [City]"
# Output: SEO-Files/ subfolder (auto-created)
# USAGE: python generate_geo_pages.py
# Run from: C:\Users\rbend\Desktop\GOLFVILLA-WEBSITE\Funnel Websites\golfvilla-com\

import os

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SEO-Files")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── NAV / FOOTER ─────────────────────────────────────────────────────────────

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
<div class="mobile-menu">
  <button class="mobile-close">×</button>
  <a href="/">Home</a>
  <a href="/what-is-a-golf-villa">What is a Golf Villa?</a>
  <a href="/caribbean-golf-villa">Caribbean</a>
  <a href="/cap-cana-golf-villa">Cap Cana</a>
  <a href="https://www.espadavilla.com">Book Villa Espada →</a>
</div>"""

FOOTER = """<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <span class="logo-top">Golf Villa</span>
      <span class="logo-sub">The World's Premier Golf Villa</span>
      <p>GolfVilla.com — the authoritative guide to private golf villa rentals worldwide, and home to Villa Espada at Cap Cana.</p>
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


# ─── PAGE TEMPLATE ─────────────────────────────────────────────────────────────

def make_geo_page(city, state_or_country, region_label, slug, is_international=False):
    """Generate a geo-targeted golf villa page for a given city."""
    location = f"{city}, {state_or_country}"
    title = f"Golf Villa {city} | Private Golf Villa Rental from {city} · GolfVilla.com"
    meta = (f"Planning a private golf villa trip from {city}? Discover Villa Espada — the world's finest golf villa "
            f"on Punta Espada Fairway 5 in Cap Cana, Dominican Republic. Member tee times, private chef, 8 bedrooms.")
    canonical = f"https://www.golfvilla.com/SEO-Files/golf-villa-{slug}"

    if is_international:
        flight_note = (f"Cap Cana is served by Punta Cana International Airport (PUJ), with connecting flights from "
                       f"{city} typically routed through major hubs. The drive from PUJ to the villa is 20 minutes, "
                       f"with private transfers arranged by the villa concierge.")
        origin_context = f"golfers traveling from {city}"
    else:
        flight_note = (f"Punta Cana International Airport (PUJ) is the closest airport to Cap Cana, served by direct "
                       f"nonstop flights from numerous major US cities. Golfers from {city} typically connect through "
                       f"major hubs including Atlanta, Miami, New York, or Charlotte — with total travel time of "
                       f"5–8 hours depending on routing. Private villa transfers from PUJ are included.")
        origin_context = f"golfers from {city}"

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
  <li>Golf Villa from {city}</li>
</ol></div>

<section class="page-hero">
  <div class="page-hero-content">
    <span class="overline">Golf Villa · {location} · Cap Cana, Dominican Republic</span>
    <h1>Golf Villa from {city}.<br><em>The World's Finest.</em></h1>
    <p>For {origin_context}: Villa Espada in Cap Cana is the world's premier private golf villa. Fairway 5, Punta Espada — the #1 ranked resort course in Latin America. Member tee times, private chef, 8 bedrooms, full staff.</p>
  </div>
</section>

<div class="article-body">
  <div class="container">
    <main class="article-main">

      <div class="article-section fade-up">
        <h2>The World's Best Golf Villa Trip from {city}</h2>
        <div class="gold-divider"></div>
        <p>If you are organizing a private golf villa trip from {city} — whether it's an annual golf group, a bachelor party, a corporate outing, or a family vacation — Cap Cana in the Dominican Republic is the destination that changes the conversation. Villa Espada is the golf villa that makes it happen.</p>
        <p>The villa sits directly on Fairway 5 of Punta Espada — the Jack Nicklaus Signature design that has been ranked the #1 resort course in Latin America and the Caribbean for over a decade. Five of its holes play directly along the Caribbean Sea. In November 2025, a second Nicklaus Signature course opened next door: Las Iguanas, with three consecutive oceanside holes and a protected iguana nature reserve woven through the layout.</p>
        <p>Your group will have the entire villa — 8 bedrooms, private pool, chef, butler, two golf carts, member tee time access to both courses. No other guests. No shared amenities. Just your group, an extraordinary villa, and two world-class courses to play.</p>
      </div>

      <div class="article-section fade-up">
        <h2>What's Included — Golf Villa from {city}</h2>
        <div class="gold-divider"></div>
        <p><strong>Accommodation:</strong> 8 ensuite bedrooms across 10,000+ square feet of private living space. Infinity pool overlooking Punta Espada Fairway 5. Multiple terraces, dining rooms, and living areas designed for large groups. Up to 22 guests.</p>
        <p><strong>Private Chef:</strong> Breakfast before the round, lunch service, full dinner each evening. Menus tailored to your group, dietary accommodations handled, occasion cooking available (welcome dinners, farewell nights, any special event during your stay).</p>
        <p><strong>Butler & Concierge:</strong> Your personal butler pre-books tee times at member/owner-tier rates at both Punta Espada and Las Iguanas before you arrive. Restaurant reservations, excursions, private transfers, in-villa entertainment — all arranged on request.</p>
        <p><strong>Golf Carts:</strong> Two six-person golf carts, fueled and available throughout your stay. Drive directly from the villa to the first tee at Punta Espada. Use them to explore Cap Cana's resort grounds, access the marina, or move your group between villa and clubhouse.</p>
        <p><strong>Airport Transfers:</strong> Private vehicle pickup and drop-off at Punta Cana International Airport (PUJ). {flight_note}</p>
        <p><strong>Member Tee Time Access:</strong> Punta Espada and Las Iguanas at owner/member-tier green fee rates. For {origin_context} playing four rounds over a 7-night stay, the savings versus public rack rates are significant and real.</p>
      </div>

      <div class="article-section fade-up">
        <h2>Punta Espada — The Course You're Going For</h2>
        <div class="gold-divider"></div>
        <p>Punta Espada is a Jack Nicklaus Signature design built in 2006 inside the Cap Cana resort in the Dominican Republic. It has been ranked the #1 resort course in Latin America and the Caribbean consistently for nearly two decades. Five holes play directly along the Caribbean Sea, with dramatic coral rock coastline, ocean wind, and Nicklaus's signature strategic bunkering creating one of the most visually memorable rounds of golf available anywhere in the Americas.</p>
        <p>The course is known for its demanding Par-3 holes, particularly the signature oceanside holes where the green sits at the edge of the cliff above the Caribbean. The fairways are consistently in tournament condition. The staff-to-player ratio and service standard matches the world's best resort courses in Scotland and Ireland. Visitors consistently rank it among the top five rounds they have ever played, regardless of how widely they have traveled for golf.</p>
        <p>Villa Espada sits on Fairway 5. You walk out the back of the villa and you are on the course. That proximity — that immediacy — is what distinguishes this golf villa from any other arrangement in the Caribbean.</p>
      </div>

      <div class="article-section fade-up">
        <h2>Rates & Availability</h2>
        <div class="gold-divider"></div>
        <p>Villa Espada rates: <strong>$2,500/night</strong> (May–October low season, 3-night minimum) · <strong>$4,500/night</strong> (November–April peak season, 5-night minimum) · <strong>$6,500/night</strong> (Christmas, New Year's, Easter, 7-night minimum).</p>
        <p>All rates include private chef, butler, housekeeping, two golf carts, member tee times at Punta Espada and Las Iguanas, and private airport transfers. +18% Dominican Republic government tax. Green fees billed at member/owner tier separately at time of play.</p>
        <p>For groups of 8 from {city} splitting the cost: peak season pricing is approximately $562/person/night, fully all-inclusive for accommodation, staff, and golf access. That compares favorably to 8 hotel rooms + 8 restaurant dinners + 8 individual transfers + public green fee rates at the same courses.</p>
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
        <h4>Quick Facts</h4>
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
        <h4>Golf Guides</h4>
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
    <h2 style="color:var(--white);">Book the Golf Villa from {city}</h2>
    <p style="color:rgba(255,255,255,0.7);">Villa Espada · Punta Espada Fairway 5 · Cap Cana. The world's finest golf villa. Member tee times, private chef, 8 bedrooms, full staff.</p>
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
      <div class="related-card fade-up"><span class="overline">Cap Cana</span><h4><a href="/cap-cana-golf-villa">Cap Cana Golf Villa — Full Guide</a></h4><p>The world's finest golf villa destination. Two Nicklaus courses, private villa, full staff.</p></div>
      <div class="related-card fade-up"><span class="overline">Caribbean</span><h4><a href="/caribbean-golf-villa">Caribbean Golf Villa Guide</a></h4><p>The best private golf villa destinations across the Caribbean.</p></div>
      <div class="related-card fade-up"><span class="overline">Featured Villa</span><h4><a href="https://www.espadavilla.com">Villa Espada · Book Now</a></h4><p>The world's premier golf villa. Direct booking at espadavilla.com.</p></div>
    </div>
  </div>
</section>

{FOOTER}
</body>
</html>"""


# ─── CITY DATA ─────────────────────────────────────────────────────────────────

# US Cities: (city, state, region_label)
US_CITIES = [
    ("New York", "NY", "Northeast"), ("Los Angeles", "CA", "West Coast"),
    ("Chicago", "IL", "Midwest"), ("Houston", "TX", "South"),
    ("Phoenix", "AZ", "Southwest"), ("Philadelphia", "PA", "Northeast"),
    ("San Antonio", "TX", "South"), ("San Diego", "CA", "West Coast"),
    ("Dallas", "TX", "South"), ("San Jose", "CA", "West Coast"),
    ("Austin", "TX", "South"), ("Jacksonville", "FL", "Southeast"),
    ("Fort Worth", "TX", "South"), ("Columbus", "OH", "Midwest"),
    ("Charlotte", "NC", "Southeast"), ("Indianapolis", "IN", "Midwest"),
    ("San Francisco", "CA", "West Coast"), ("Seattle", "WA", "Northwest"),
    ("Denver", "CO", "Mountain"), ("Nashville", "TN", "South"),
    ("Oklahoma City", "OK", "South"), ("El Paso", "TX", "Southwest"),
    ("Washington DC", "DC", "Mid-Atlantic"), ("Boston", "MA", "Northeast"),
    ("Las Vegas", "NV", "Southwest"), ("Louisville", "KY", "South"),
    ("Memphis", "TN", "South"), ("Portland", "OR", "Northwest"),
    ("Atlanta", "GA", "Southeast"), ("Baltimore", "MD", "Mid-Atlantic"),
    ("Milwaukee", "WI", "Midwest"), ("Albuquerque", "NM", "Southwest"),
    ("Tucson", "AZ", "Southwest"), ("Fresno", "CA", "West Coast"),
    ("Sacramento", "CA", "West Coast"), ("Kansas City", "MO", "Midwest"),
    ("Mesa", "AZ", "Southwest"), ("Omaha", "NE", "Midwest"),
    ("Raleigh", "NC", "Southeast"), ("Colorado Springs", "CO", "Mountain"),
    ("Virginia Beach", "VA", "Mid-Atlantic"), ("Minneapolis", "MN", "Midwest"),
    ("Tampa", "FL", "Southeast"), ("New Orleans", "LA", "South"),
    ("Cleveland", "OH", "Midwest"), ("Wichita", "KS", "Midwest"),
    ("Arlington", "TX", "South"), ("Bakersfield", "CA", "West Coast"),
    ("Aurora", "CO", "Mountain"), ("Anaheim", "CA", "West Coast"),
    ("Santa Ana", "CA", "West Coast"), ("Corpus Christi", "TX", "South"),
    ("Riverside", "CA", "West Coast"), ("Lexington", "KY", "South"),
    ("St Louis", "MO", "Midwest"), ("Pittsburgh", "PA", "Northeast"),
    ("Anchorage", "AK", "Northwest"), ("Stockton", "CA", "West Coast"),
    ("Cincinnati", "OH", "Midwest"), ("St Paul", "MN", "Midwest"),
    ("Greensboro", "NC", "Southeast"), ("Toledo", "OH", "Midwest"),
    ("Newark", "NJ", "Northeast"), ("Plano", "TX", "South"),
    ("Henderson", "NV", "Southwest"), ("Orlando", "FL", "Southeast"),
    ("Chandler", "AZ", "Southwest"), ("Laredo", "TX", "South"),
    ("Madison", "WI", "Midwest"), ("Durham", "NC", "Southeast"),
    ("Lubbock", "TX", "South"), ("Winston-Salem", "NC", "Southeast"),
    ("Garland", "TX", "South"), ("Glendale", "AZ", "Southwest"),
    ("Hialeah", "FL", "Southeast"), ("Reno", "NV", "West"),
    ("Baton Rouge", "LA", "South"), ("Irvine", "CA", "West Coast"),
    ("Chesapeake", "VA", "Mid-Atlantic"), ("Irving", "TX", "South"),
    ("Scottsdale", "AZ", "Southwest"), ("North Las Vegas", "NV", "Southwest"),
    ("Fremont", "CA", "West Coast"), ("Gilbert", "AZ", "Southwest"),
    ("San Bernardino", "CA", "West Coast"), ("Birmingham", "AL", "Southeast"),
    ("Rochester", "NY", "Northeast"), ("Richmond", "VA", "Mid-Atlantic"),
    ("Spokane", "WA", "Northwest"), ("Des Moines", "IA", "Midwest"),
    ("Montgomery", "AL", "Southeast"), ("Modesto", "CA", "West Coast"),
    ("Fayetteville", "NC", "Southeast"), ("Tacoma", "WA", "Northwest"),
    ("Shreveport", "LA", "South"), ("Fontana", "CA", "West Coast"),
    ("Moreno Valley", "CA", "West Coast"), ("Glendale", "CA", "West Coast"),
    ("Akron", "OH", "Midwest"), ("Yonkers", "NY", "Northeast"),
    ("Augusta", "GA", "Southeast"), ("Little Rock", "AR", "South"),
    ("Huntington Beach", "CA", "West Coast"), ("Columbus", "GA", "Southeast"),
    ("Grand Rapids", "MI", "Midwest"), ("Salt Lake City", "UT", "Mountain"),
    ("Tallahassee", "FL", "Southeast"), ("Huntsville", "AL", "Southeast"),
    ("Worcester", "MA", "Northeast"), ("Knoxville", "TN", "Southeast"),
    ("Providence", "RI", "Northeast"), ("Brownsville", "TX", "South"),
    ("Newport News", "VA", "Mid-Atlantic"), ("Santa Clarita", "CA", "West Coast"),
    ("Garden Grove", "CA", "West Coast"), ("Oceanside", "CA", "West Coast"),
    ("Fort Lauderdale", "FL", "Southeast"), ("Chattanooga", "TN", "Southeast"),
    ("Rancho Cucamonga", "CA", "West Coast"), ("Santa Rosa", "CA", "West Coast"),
    ("Port Arthur", "TX", "South"), ("Tempe", "AZ", "Southwest"),
    ("Cape Coral", "FL", "Southeast"), ("Oxnard", "CA", "West Coast"),
    ("Eugene", "OR", "Northwest"), ("Peoria", "IL", "Midwest"),
    ("Salem", "OR", "Northwest"), ("Cary", "NC", "Southeast"),
    ("Palmdale", "CA", "West Coast"), ("Springfield", "MO", "Midwest"),
    ("Fort Collins", "CO", "Mountain"), ("Jackson", "MS", "South"),
    ("Alexandria", "VA", "Mid-Atlantic"), ("Hayward", "CA", "West Coast"),
    ("Lancaster", "CA", "West Coast"), ("Salinas", "CA", "West Coast"),
    ("Sunnyvale", "CA", "West Coast"), ("Pomona", "CA", "West Coast"),
    ("Escondido", "CA", "West Coast"), ("Torrance", "CA", "West Coast"),
    ("Pasadena", "TX", "South"), ("Paterson", "NJ", "Northeast"),
    ("Surprise", "AZ", "Southwest"), ("Roseville", "CA", "West Coast"),
    ("Bridgeport", "CT", "Northeast"), ("Macon", "GA", "Southeast"),
    ("Kansas City", "KS", "Midwest"), ("Savannah", "GA", "Southeast"),
    ("Syracuse", "NY", "Northeast"), ("Dayton", "OH", "Midwest"),
    ("Hollywood", "FL", "Southeast"), ("Lakewood", "CO", "Mountain"),
    ("Colorado Springs", "CO", "Mountain"), ("Pomona", "CA", "West Coast"),
    ("Pembroke Pines", "FL", "Southeast"), ("Clarksville", "TN", "South"),
    ("Mesquite", "TX", "South"), ("Killeen", "TX", "South"),
    ("Waco", "TX", "South"), ("McAllen", "TX", "South"),
    ("Metairie", "LA", "South"), ("Coral Springs", "FL", "Southeast"),
]

# International cities: (city, country, region_label)
INTERNATIONAL_CITIES = [
    ("Toronto", "Canada", "North America"), ("Montreal", "Canada", "North America"),
    ("Vancouver", "Canada", "North America"), ("Calgary", "Canada", "North America"),
    ("Ottawa", "Canada", "North America"), ("London", "UK", "Europe"),
    ("Manchester", "UK", "Europe"), ("Birmingham", "UK", "Europe"),
    ("Edinburgh", "Scotland", "Europe"), ("Glasgow", "Scotland", "Europe"),
    ("Dublin", "Ireland", "Europe"), ("Paris", "France", "Europe"),
    ("Frankfurt", "Germany", "Europe"), ("Amsterdam", "Netherlands", "Europe"),
    ("Madrid", "Spain", "Europe"), ("Barcelona", "Spain", "Europe"),
    ("Bogota", "Colombia", "South America"), ("Medellin", "Colombia", "South America"),
    ("Mexico City", "Mexico", "North America"), ("Monterrey", "Mexico", "North America"),
    ("Buenos Aires", "Argentina", "South America"), ("Sao Paulo", "Brazil", "South America"),
    ("Lima", "Peru", "South America"), ("Santiago", "Chile", "South America"),
    ("Caracas", "Venezuela", "South America"), ("Panama City", "Panama", "Central America"),
    ("San Jose", "Costa Rica", "Central America"), ("Guatemala City", "Guatemala", "Central America"),
    ("Sydney", "Australia", "Pacific"), ("Melbourne", "Australia", "Pacific"),
    ("Dubai", "UAE", "Middle East"), ("Johannesburg", "South Africa", "Africa"),
    ("Tokyo", "Japan", "Asia"), ("Singapore", "Singapore", "Asia"),
]


# ─── GENERATE PAGES ────────────────────────────────────────────────────────────

def city_to_slug(city):
    return city.lower().replace(" ", "-").replace(",", "").replace(".", "")

count = 0

# US cities
for city, state, region in US_CITIES:
    slug = f"golf-villa-{city_to_slug(city)}"
    html = make_geo_page(city, state, region, slug, is_international=False)
    path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    count += 1

# International cities
for city, country, region in INTERNATIONAL_CITIES:
    slug = f"golf-villa-{city_to_slug(city)}"
    html = make_geo_page(city, country, region, slug, is_international=True)
    path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    count += 1

print(f"✅ Generated {count} geo pages → SEO-Files/")
print(f"   Files: golf-villa-[city].html")
print(f"   US cities: {len(US_CITIES)} | International: {len(INTERNATIONAL_CITIES)}")
