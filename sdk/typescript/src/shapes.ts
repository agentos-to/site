// Auto-generated from shape YAML — do not edit.
// Generated from 94 shapes.
// Regenerate with: python generate.py --lang typescript

export interface Account {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accountType?: string;
    bio?: string;
    color?: string;
    display?: string;
    displayName?: string;
    email?: string;
    handle?: string;
    identifier?: string;
    isActive?: boolean;
    issuer?: string;
    joinedDate?: string;
    lastActive?: string;
    lastProfileFetch?: string;
    metadata?: unknown;
    phone?: string;
    userId?: string;
    at?: Actor;
    authenticatedVia?: Account;
    followers?: Account[];
    follows?: Account[];
    operator?: Actor;
    owner?: Person;
    previousIdentity?: Account[];
    protocol?: Protocol;
    via?: Product;
}

export interface Activity {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    action?: string;
    at?: string;
    changedKeys?: string[];
    duration?: number;
    success?: boolean;
    toolName?: string;
    folder?: List;
    session?: McpSession;
}

export interface Actor {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actorType?: string;
}

export interface Agent {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actorType?: string;
    model?: string;
    provider?: string;
    sessionId?: string;
}

export interface Aircraft {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aisle?: string;
    availability?: string;
    barcode?: string;
    calories?: number;
    categories?: string[];
    category?: string;
    currency?: string;
    customizationGroups?: unknown;
    department?: string;
    discontinued?: string;
    iataCode?: string;
    icaoCode?: string;
    images?: unknown;
    model?: string;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    price?: string;
    priceAmount?: number;
    quantity?: number;
    rangeKm?: number;
    released?: string;
    seatCapacity?: number;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    variant?: string;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
    brand?: Brand;
    creator?: Actor[];
    inspiredBy?: Product[];
    manufacturer?: Organization;
    tagged?: Tag[];
}

export interface Airline {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actorType?: string;
    alliance?: string;
    callsign?: string;
    country?: string;
    founded?: string;
    iataCode?: string;
    icaoCode?: string;
    industry?: string;
    domain?: Domain;
    headquarters?: Place;
    member?: Person[];
    website?: Website;
}

export interface Airport {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    city?: string;
    country?: string;
    countryCode?: string;
    elevationFt?: number;
    iataCode?: string;
    icaoCode?: string;
    terminalCount?: number;
    timezone?: string;
    location?: Place;
    operator?: Organization;
}

export interface App {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    defaultView?: string;
    handles?: string[];
    iconRole?: string;
    isSystem?: boolean;
    route?: string;
}

export interface Book {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    datePublished?: string;
    content?: string;
    aisle?: string;
    availability?: string;
    awardsWon?: string[];
    barcode?: string;
    calories?: number;
    categories?: string[];
    category?: string;
    characters?: string[];
    copyrightYear?: number;
    coverage?: string;
    currency?: string;
    customizationGroups?: unknown;
    dateCreated?: unknown;
    department?: string;
    description?: string;
    discontinued?: string;
    format?: string;
    genres?: string[];
    images?: unknown;
    isbn?: string;
    isbn13?: string;
    language?: string;
    license?: string;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    originalTitle?: string;
    pages?: number;
    places?: string[];
    price?: string;
    priceAmount?: number;
    quantity?: number;
    released?: string;
    series?: string;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    tags?: string[];
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
    author?: Person;
    brand?: Brand;
    contributors?: Person[];
    copyrightHolder?: Person;
    creator?: Actor[];
    inspiredBy?: Product[];
    manufacturer?: Organization;
    publisher?: Organization;
    tagged?: Tag[];
    writtenBy?: Person;
}

export interface BookingOffer {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    approvedAt?: string;
    baseAmount?: number;
    blob?: string;
    cartId?: string;
    checkoutUrl?: string;
    conditions?: unknown;
    confirmEndpoint?: string;
    contactEmail?: string;
    contactPhone?: string;
    currency?: string;
    expiresAt?: string;
    feesAmount?: number;
    hasVoidWindow?: boolean;
    isChangeable?: boolean;
    isRefundable?: boolean;
    itineraryHash?: string;
    preparedAt?: string;
    presentedAt?: string;
    referenceNumber?: string;
    review?: string;
    signature?: string;
    signatureAlg?: string;
    signedBy?: string;
    status?: string;
    taxAmount?: number;
    totalAmount?: number;
    voidWindowEndsAt?: string;
    account?: Account;
    at?: Actor;
    becameReservation?: Reservation;
    becameTransaction?: Transaction;
    billingAddress?: Place;
    broker?: Actor;
    buyers?: Person[];
    derivedFrom?: Offer;
    fares?: Fare[];
    guests?: Person[];
    membership?: Membership;
    paymentMethod?: PaymentMethod;
    reservedItems?: Pass[];
    taxLines?: TaxLine[];
    trips?: Trip[];
    underName?: Person;
}

export interface Bookmark {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    target?: unknown;
}

export interface Branch {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    ahead?: number;
    behind?: number;
    commit?: string;
    isCurrent?: boolean;
    isRemote?: boolean;
    upstream?: string;
    repository?: Repository;
}

export interface Brand {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    country?: string;
    founded?: string;
    primaryColor?: string;
    tagline?: string;
    textColor?: string;
    logo?: Image;
    ownedBy?: Organization;
    website?: Website;
}

export interface Calendar {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accessRole?: string;
    backgroundColor?: string;
    calendarId?: string;
    color?: string;
    foregroundColor?: string;
    isPrimary?: boolean;
    isReadonly?: boolean;
    source?: string;
    timezone?: string;
    at?: Actor;
    events?: Event[];
    owner?: Person;
}

export interface Channel {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    banner?: string;
    subscriberCount?: number;
    at?: Actor;
}

export interface Class {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    activityType?: string;
    allDay?: boolean;
    articleUrl?: string;
    capacity?: number;
    crewIds?: string[];
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    eventType?: string;
    flightNumber?: number;
    icalUid?: string;
    isFull?: boolean;
    landingOutcomes?: unknown;
    launchpadId?: string;
    patchImage?: string;
    properties?: unknown;
    recurrence?: string[];
    reusedBoosters?: string[];
    rocketId?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    spotsRemaining?: number;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
    webcastUrl?: string;
    wikipediaUrl?: string;
    at?: Actor;
    attachments?: File[];
    creator?: Person;
    instructor?: Person;
    involves?: Person[];
    location?: Place;
    organizer?: Person;
    person?: Person;
    venue?: Place;
}

export interface Community {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allowCrypto?: boolean;
    memberCount?: number;
    privacy?: string;
    subscriberCount?: number;
    at?: Actor;
}

export interface Conversation {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accountEmail?: string;
    cwd?: string;
    gitBranch?: string;
    historyId?: string;
    isArchived?: boolean;
    isGroup?: boolean;
    messageCount?: number;
    source?: string;
    unreadCount?: number;
    at?: Actor;
    in?: List;
    message?: Message[];
    participant?: Actor[];
}

export interface CreativeWork {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    datePublished?: string;
    content?: string;
    copyrightYear?: number;
    coverage?: string;
    dateCreated?: unknown;
    description?: string;
    language?: string;
    license?: string;
    tags?: string[];
    author?: Person;
    contributors?: Person[];
    copyrightHolder?: Person;
    publisher?: Organization;
}

export interface Credential {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    domain?: string;
    expiresAt?: string;
    identifier?: string;
    itemType?: string;
    lastVerified?: string;
    obtainedAt?: string;
    refreshable?: boolean;
    source?: string;
    storeRowId?: number;
    account?: Account;
    at?: Organization;
    writtenBy?: Skill;
}

export interface DnsRecord {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    domain?: string;
    priority?: number;
    recordId?: string;
    recordName?: string;
    recordType?: string;
    ttl?: number;
    type?: string;
    values?: string[];
}

export interface Document {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    datePublished?: string;
    content?: string;
    abstract?: string;
    contentType?: string;
    encoding?: string;
    filename?: string;
    format?: string;
    kind?: string;
    language?: string;
    lineCount?: number;
    mimeType?: string;
    path?: string;
    sha?: string;
    size?: number;
    tableOfContents?: string;
    wordCount?: number;
    attachedTo?: Message;
    author?: Actor;
    citedBy?: Document[];
    references?: Document[];
    repository?: Repository;
}

export interface Domain {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    autoRenew?: boolean;
    createdAt?: string;
    expiresAt?: string;
    nameservers?: string[];
    registrar?: string;
    status?: string;
}

export interface Email {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accountEmail?: string;
    attachments?: unknown;
    authResults?: string;
    bccRaw?: string;
    bodyHtml?: string;
    ccRaw?: string;
    conversationId?: string;
    deliveredTo?: string;
    draftId?: string;
    hasAttachments?: boolean;
    inReplyTo?: string;
    isAutomated?: boolean;
    isDraft?: boolean;
    isOutgoing?: boolean;
    isSent?: boolean;
    isSpam?: boolean;
    isStarred?: boolean;
    isTrash?: boolean;
    isUnread?: boolean;
    listId?: string;
    mailer?: string;
    manageSubscription?: string;
    messageId?: string;
    precedence?: string;
    references?: string;
    replyTo?: string;
    returnPath?: string;
    sizeEstimate?: number;
    subject?: string;
    toRaw?: string;
    unsubscribe?: string;
    unsubscribeOneClick?: boolean;
    at?: Actor;
    bcc?: Account[];
    cc?: Account[];
    ccDomain?: Domain[];
    domain?: Domain;
    from?: Account;
    inConversation?: Conversation;
    repliesTo?: Message;
    tag?: Tag[];
    to?: Account[];
    toDomain?: Domain[];
    toolCalls?: ToolCall[];
}

export interface Episode {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    durationMs?: number;
    episodeNumber?: number;
    seasonNumber?: number;
    guest?: Person[];
    series?: Podcast;
    transcribe?: Transcript;
}

export interface Event {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allDay?: boolean;
    articleUrl?: string;
    crewIds?: string[];
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    eventType?: string;
    flightNumber?: number;
    icalUid?: string;
    landingOutcomes?: unknown;
    launchpadId?: string;
    patchImage?: string;
    properties?: unknown;
    recurrence?: string[];
    reusedBoosters?: string[];
    rocketId?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
    webcastUrl?: string;
    wikipediaUrl?: string;
    at?: Actor;
    attachments?: File[];
    creator?: Person;
    involves?: Person[];
    location?: Place;
    organizer?: Person;
    person?: Person;
}

export interface Fare {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    basePrice?: number;
    bookingCode?: string;
    changeable?: boolean;
    class?: string;
    components?: number;
    conditions?: unknown;
    currency?: string;
    fareFamily?: string;
    identifier?: string;
    milesEarned?: number;
    passengerType?: string;
    pointsEarned?: number;
    productType?: string;
    refundable?: boolean;
    restrictions?: string[];
    at?: Actor;
    earnsInto?: Membership;
    for?: Trip;
    legs?: Leg[];
    offer?: Offer;
    reservation?: Reservation;
    taxLines?: TaxLine[];
}

export interface File {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    encoding?: string;
    filename?: string;
    format?: string;
    kind?: string;
    lineCount?: number;
    mimeType?: string;
    path?: string;
    sha?: string;
    size?: number;
    attachedTo?: Message;
    repository?: Repository;
}

export interface FinancialAccount {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accountId?: string;
    accountNumber?: string;
    accountType?: string;
    available?: number;
    balance?: number;
    cardType?: string;
    creditLimit?: number;
    currency?: string;
    expiresAt?: string;
    identifier?: string;
    interestRate?: number;
    last4?: string;
    minimumPayment?: number;
    paymentDueDate?: string;
    routingNumber?: string;
    accessedVia?: Account;
    at?: Actor;
    owner?: Person;
}

export interface Flight {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    arrivalTime?: string;
    cabinClass?: string;
    carbonEmissions?: unknown;
    departureTime?: string;
    duration?: string;
    durationMinutes?: number;
    flightNumber?: string;
    layoverMinutes?: number;
    polyline?: string;
    sequence?: number;
    stops?: number;
    trace?: unknown;
    tracePointCount?: number;
    vehicleType?: string;
    aircraft?: Aircraft;
    airline?: Airline;
    arrivesAt?: Airport;
    carrier?: Organization;
    departsFrom?: Airport;
    destination?: Place;
    origin?: Place;
    trip?: Trip;
}

export interface Font {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    datePublished?: string;
    content?: string;
    copyrightYear?: number;
    coverage?: string;
    dateCreated?: unknown;
    description?: string;
    designerUrl?: string;
    family?: string;
    formats?: string[];
    genericFamily?: string;
    glyphCount?: number;
    language?: string;
    license?: string;
    licenseInfoUrl?: string;
    postscriptName?: string;
    scripts?: string[];
    styles?: string[];
    tags?: string[];
    vendorUrl?: string;
    weights?: number[];
    author?: Person;
    contributors?: Person[];
    copyrightHolder?: Person;
    publisher?: Organization;
}

export interface GitCommit {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    datePublished?: string;
    content?: string;
    additions?: number;
    committedAt?: string;
    deletions?: number;
    filesChanged?: number;
    message?: string;
    sha?: string;
    shortHash?: string;
    author?: Account;
    committer?: Account;
    parent?: GitCommit;
    repository?: Repository;
}

export interface Group {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    category?: string;
    memberCount?: number;
}

export interface Hardware {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aisle?: string;
    availability?: string;
    barcode?: string;
    calories?: number;
    categories?: string[];
    category?: string;
    currency?: string;
    customizationGroups?: unknown;
    department?: string;
    discontinued?: string;
    images?: unknown;
    modelNumber?: string;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    price?: string;
    priceAmount?: number;
    quantity?: number;
    released?: string;
    serialNumber?: string;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    specs?: unknown;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
    brand?: Brand;
    creator?: Actor[];
    inspiredBy?: Product[];
    manufacturer?: Organization;
    tagged?: Tag[];
}

export interface HealthBiomarker {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    analyteType?: string;
    category?: string;
    description?: string;
    loincCode?: string;
    measure?: string;
    unit?: string;
    panels?: HealthPanel[];
}

export interface HealthCondition {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    abatementDate?: string;
    bodySite?: string;
    clinicalArea?: string;
    clinicalStatus?: string;
    icd10Code?: string;
    mitigation?: string;
    onsetDate?: string;
    proximity?: string;
    severity?: string;
    snomedCode?: string;
    verificationStatus?: string;
    evidence?: File[];
    subject?: Person;
}

export interface HealthImmunization {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allDay?: boolean;
    articleUrl?: string;
    crewIds?: string[];
    currentUrl?: string;
    cvxCode?: string;
    dateAdministered?: string;
    dateUpdated?: string;
    diseaseTarget?: string;
    distinctId?: string;
    doseNumber?: number;
    endDate?: string;
    eventType?: string;
    flightNumber?: number;
    icalUid?: string;
    landingOutcomes?: unknown;
    launchpadId?: string;
    lotNumber?: string;
    manufacturer?: string;
    notes?: string;
    patchImage?: string;
    properties?: unknown;
    recurrence?: string[];
    reusedBoosters?: string[];
    rocketId?: string;
    route?: string;
    seriesDoses?: number;
    showAs?: string;
    site?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
    webcastUrl?: string;
    wikipediaUrl?: string;
    administeredAt?: HealthLab;
    at?: Actor;
    attachments?: File[];
    creator?: Person;
    evidence?: File[];
    involves?: Person[];
    location?: Place;
    organizer?: Person;
    person?: Person;
    subject?: Person;
}

export interface HealthLab {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accreditation?: string;
    actorType?: string;
    cliaNumber?: string;
    founded?: string;
    industry?: string;
    labType?: string;
    networkName?: string;
    domain?: Domain;
    headquarters?: Place;
    member?: Person[];
    website?: Website;
}

export interface HealthObservation {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    community?: string;
    effectiveDate?: string;
    externalUrl?: string;
    flag?: string;
    indexedAt?: string;
    notes?: string;
    postId?: string;
    refHigh?: number;
    refLow?: number;
    refText?: string;
    resultType?: string;
    score?: number;
    similarity?: number;
    status?: string;
    unit?: string;
    value?: number;
    valueText?: string;
    document?: File;
    fromPanel?: HealthPanel;
    measures?: HealthBiomarker;
    reportedRange?: HealthReferenceRange;
    subject?: Person;
}

export interface HealthPanel {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    defaultView?: string;
    description?: string;
    effectiveDate?: string;
    fasting?: boolean;
    iconSize?: number;
    isDefault?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    listId?: string;
    listType?: string;
    orderingMode?: string;
    panelCode?: string;
    path?: string;
    privacy?: string;
    sortBy?: string;
    at?: Actor;
    backgroundImage?: Image;
    belongsTo?: Account;
    contains?: unknown[];
    document?: File;
    performedAt?: HealthLab;
    subject?: Person;
}

export interface HealthProcedure {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allDay?: boolean;
    articleUrl?: string;
    bodySite?: string;
    cptCode?: string;
    crewIds?: string[];
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    eventType?: string;
    findings?: string;
    flightNumber?: number;
    followUp?: string;
    icalUid?: string;
    landingOutcomes?: unknown;
    launchpadId?: string;
    outcome?: string;
    patchImage?: string;
    performedDate?: string;
    procedureType?: string;
    properties?: unknown;
    recurrence?: string[];
    reusedBoosters?: string[];
    rocketId?: string;
    showAs?: string;
    snomedCode?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
    webcastUrl?: string;
    wikipediaUrl?: string;
    at?: Actor;
    attachments?: File[];
    creator?: Person;
    evidence?: File[];
    involves?: Person[];
    location?: Place;
    organizer?: Person;
    performedAt?: HealthLab;
    performer?: Person;
    person?: Person;
    subject?: Person;
    treats?: HealthCondition;
}

export interface HealthReferenceRange {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    ageHigh?: number;
    ageLow?: number;
    category?: string;
    fasting?: boolean;
    gestationalAge?: string;
    high?: number;
    low?: number;
    method?: string;
    pregnancy?: string;
    provenance?: string;
    refText?: string;
    sex?: string;
    timeOfDay?: string;
    unit?: string;
    validFrom?: string;
    validTo?: string;
    analyte?: HealthBiomarker;
    issuingLab?: HealthLab;
}

export interface Icon {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    datePublished?: string;
    content?: string;
    component?: string;
    copyrightYear?: number;
    coverage?: string;
    dateCreated?: unknown;
    description?: string;
    dimension?: number;
    format?: string;
    language?: string;
    license?: string;
    purpose?: string;
    style?: string;
    tags?: string[];
    author?: Person;
    contributors?: Person[];
    copyrightHolder?: Person;
    publisher?: Organization;
}

export interface Image {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    datePublished?: string;
    content?: string;
    altText?: string;
    appName?: string;
    copyrightYear?: number;
    coverage?: string;
    dateCreated?: unknown;
    description?: string;
    displayId?: number;
    displayIndex?: number;
    encoding?: string;
    filename?: string;
    format?: string;
    height?: number;
    kind?: string;
    language?: string;
    license?: string;
    lineCount?: number;
    mimeType?: string;
    path?: string;
    sha?: string;
    size?: number;
    tags?: string[];
    width?: number;
    windowId?: number;
    attachedTo?: Message;
    author?: Person;
    contributors?: Person[];
    copyrightHolder?: Person;
    publisher?: Organization;
    repository?: Repository;
}

export interface Invitation {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    acceptedAt?: string;
    email?: string;
    expiresAt?: string;
    invitationType?: string;
    message?: string;
    revokedAt?: string;
    role?: string;
    status?: string;
    token?: string;
    at?: Actor;
    invitee?: Account;
    inviter?: Account;
    organization?: Organization;
}

export interface Leg {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    arrivalTime?: string;
    cabinClass?: string;
    carbonEmissions?: unknown;
    departureTime?: string;
    duration?: string;
    durationMinutes?: number;
    flightNumber?: string;
    layoverMinutes?: number;
    polyline?: string;
    sequence?: number;
    trace?: unknown;
    tracePointCount?: number;
    vehicleType?: string;
    aircraft?: Aircraft;
    carrier?: Organization;
    destination?: Place;
    origin?: Place;
    trip?: Trip;
}

export interface List {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    defaultView?: string;
    iconSize?: number;
    isDefault?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    listId?: string;
    listType?: string;
    orderingMode?: string;
    path?: string;
    privacy?: string;
    sortBy?: string;
    at?: Actor;
    backgroundImage?: Image;
    belongsTo?: Account;
    contains?: unknown[];
}

export interface LoadedModel {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    digest?: string;
    expiresAt?: string;
    quantization?: string;
    size?: string;
    sizeVram?: number;
    vramUsage?: string;
}

export interface McpSession {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    client?: string;
    endedAt?: string;
    gitBranch?: string;
    messageCount?: number;
    projectId?: string;
    sessionType?: string;
    startedAt?: string;
    tokenCount?: number;
    folder?: List;
    participant?: Actor;
}

export interface Meeting {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allDay?: boolean;
    articleUrl?: string;
    calendarLink?: string;
    conferenceProvider?: string;
    crewIds?: string[];
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    eventType?: string;
    flightNumber?: number;
    icalUid?: string;
    isVirtual?: boolean;
    landingOutcomes?: unknown;
    launchpadId?: string;
    meetingUrl?: string;
    patchImage?: string;
    phoneDialIn?: string;
    properties?: unknown;
    recurrence?: string[];
    reusedBoosters?: string[];
    rocketId?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
    webcastUrl?: string;
    wikipediaUrl?: string;
    at?: Actor;
    attachments?: File[];
    creator?: Person;
    involves?: Person[];
    location?: Place;
    organizer?: Person;
    person?: Person;
    transcribe?: Transcript;
}

export interface Membership {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    autoRenew?: boolean;
    billingType?: string;
    currency?: string;
    endEffectiveDate?: string;
    guestPassQuantity?: number;
    nextBillDate?: string;
    price?: number;
    startEffectiveDate?: string;
    status?: string;
    tier?: string;
    useCount?: number;
    account?: Account;
    at?: Actor;
    location?: Place;
    member?: Person;
    plan?: Product;
}

export interface Memex {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    description?: string;
    edgeCount?: number;
    filePath?: string;
    fileSize?: string;
    nodeCount?: number;
    origin?: string;
    published?: boolean;
    snapshotOf?: string;
    forkedFrom?: Memex;
    owner?: Person;
    snapshots?: Memex[];
}

export interface Message {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    conversationId?: string;
    isOutgoing?: boolean;
    isStarred?: boolean;
    at?: Actor;
    from?: Actor;
    inConversation?: Conversation;
    repliesTo?: Message;
    toolCalls?: ToolCall[];
}

export interface Model {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    contextLength?: number;
    contextWindow?: number;
    digest?: string;
    family?: string;
    format?: string;
    maxOutput?: number;
    modality?: string[];
    modelType?: string;
    parameterSize?: string;
    pricingInput?: string;
    pricingOutput?: string;
    quantization?: string;
    quantizationLevel?: string;
    size?: string;
    at?: Actor;
}

export interface Note {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    isPinned?: boolean;
    noteType?: string;
    createdBy?: Person;
    extractedFrom?: Webpage;
    references?: Note[];
}

export interface Offer {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    availability?: string;
    bookingToken?: string;
    currency?: string;
    departureToken?: string;
    offerType?: string;
    price?: number;
    validFrom?: string;
    validUntil?: string;
    for?: Product;
    offeredBy?: Organization;
    trips?: Trip[];
}

export interface Order {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    body?: string;
    currency?: string;
    deliveryDate?: string;
    deliveryFee?: number;
    deliveryInstructions?: string;
    eta?: string;
    fareBreakdown?: unknown;
    head?: string;
    interactionType?: string;
    itemStates?: unknown;
    latestArrival?: string;
    messages?: unknown;
    orderDate?: string;
    orderId?: string;
    orderUuid?: string;
    originalTotal?: string;
    originalTotalAmount?: number;
    progress?: number;
    progressTotal?: number;
    savings?: number;
    status?: string;
    subtotal?: number;
    summary?: string;
    taxes?: number;
    timeline?: unknown;
    tipAmount?: number;
    total?: string;
    totalAmount?: number;
    at?: Actor;
    contains?: Product[];
    delivery?: Trip;
    shippingAddress?: Place;
    store?: Place;
    tracking?: Webpage;
}

export interface Organization {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actorType?: string;
    founded?: string;
    industry?: string;
    domain?: Domain;
    headquarters?: Place;
    member?: Person[];
    website?: Website;
}

export interface Pass {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    boardingGroup?: string;
    checkinStatus?: string;
    currency?: string;
    depletedDate?: string;
    endEffectiveDate?: string;
    gate?: string;
    isAllDayPass?: boolean;
    nameOnTicket?: string;
    price?: number;
    purchasedDate?: string;
    purchasedQuantity?: number;
    quantity?: number;
    seatAssignment?: string;
    startEffectiveDate?: string;
    status?: string;
    terminal?: string;
    ticketClass?: string;
    ticketNumber?: string;
    useCount?: number;
    account?: Account;
    at?: Actor;
    for?: Leg;
    grantedBy?: Membership;
    holder?: Person;
    location?: Place;
    reservation?: Reservation;
    type?: Product;
}

export interface PaymentMethod {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    balance?: number;
    binRange?: string;
    brand?: string;
    currency?: string;
    customDescription?: string;
    displayName?: string;
    expMonth?: number;
    expYear?: number;
    expirationDate?: string;
    fingerprint?: string;
    holderName?: string;
    identifier?: string;
    isDefault?: boolean;
    isExpired?: boolean;
    isPrimary?: boolean;
    isSelected?: boolean;
    last4?: string;
    metadata?: unknown;
    providerTokens?: unknown;
    status?: string;
    subtype?: string;
    type?: string;
    account?: Account;
    at?: Actor;
    billingAddress?: Place;
    fundingAccount?: FinancialAccount;
    holder?: Person;
    issuer?: Actor;
    membership?: Membership;
}

export interface Person {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    about?: string;
    actorType?: string;
    additionalName?: string;
    birthday?: string;
    familyName?: string;
    gender?: string;
    givenName?: string;
    honorificPrefix?: string;
    honorificSuffix?: string;
    legalName?: string;
    maidenName?: string;
    nameOrder?: string;
    nickname?: string;
    notes?: string;
    phoneticFamilyName?: string;
    phoneticGivenName?: string;
    preferredName?: string;
    sortAs?: string;
    accounts?: Account[];
    location?: Place;
    memberships?: Membership[];
    passes?: Pass[];
    roles?: Role[];
    website?: Website;
}

export interface Place {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    accuracy?: string;
    businessStatus?: string;
    categories?: string[];
    city?: string;
    closedMessage?: string;
    country?: string;
    countryCode?: string;
    district?: string;
    eta?: string;
    featureType?: string;
    fullAddress?: string;
    googlePlaceId?: string;
    hours?: unknown;
    isOrderable?: boolean;
    latitude?: number;
    locality?: string;
    longitude?: number;
    mapboxId?: string;
    neighborhood?: string;
    phone?: string;
    placeFormatted?: string;
    postalCode?: string;
    priceLevel?: string;
    productCount?: number;
    rating?: number;
    region?: string;
    reviewCount?: number;
    street?: string;
    streetNumber?: string;
    timezone?: string;
    website?: string;
    wikidataId?: string;
    at?: Actor;
    brand?: Organization;
    offers?: Product[];
}

export interface Playlist {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    defaultView?: string;
    iconSize?: number;
    isDefault?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    listId?: string;
    listType?: string;
    orderingMode?: string;
    path?: string;
    privacy?: string;
    sortBy?: string;
    at?: Actor;
    backgroundImage?: Image;
    belongsTo?: Account;
    contains?: Video[];
}

export interface Podcast {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    feedUrl?: string;
    at?: Actor;
    episode?: Episode[];
    host?: Person[];
}

export interface Post {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    commentCount?: number;
    community?: string;
    externalUrl?: string;
    postType?: string;
    score?: number;
    at?: Actor;
    attachment?: File[];
    contains?: Video[];
    media?: Image[];
    postedBy?: Account;
    publish?: Community;
    replies?: Post[];
    repliesTo?: Post;
}

export interface Product {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aisle?: string;
    availability?: string;
    barcode?: string;
    calories?: number;
    categories?: string[];
    category?: string;
    currency?: string;
    customizationGroups?: unknown;
    department?: string;
    discontinued?: string;
    images?: unknown;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    price?: string;
    priceAmount?: number;
    quantity?: number;
    released?: string;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
    brand?: Brand;
    creator?: Actor[];
    inspiredBy?: Product[];
    manufacturer?: Organization;
    tagged?: Tag[];
}

export interface Project {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    color?: string;
    parentId?: string;
    state?: string;
    at?: Actor;
}

export interface Protocol {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    homepage?: string;
    rfc?: string;
    wikidataId?: string;
}

export interface Quote {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    context?: string;
    year?: number;
}

export interface Repository {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    defaultBranch?: string;
    forks?: number;
    isArchived?: boolean;
    isPrivate?: boolean;
    language?: string;
    license?: string;
    openIssues?: number;
    size?: number;
    stars?: number;
    topics?: string[];
    forkedFrom?: Repository;
    owner?: Account;
}

export interface Reservation {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    availableActions?: string[];
    baseAmount?: number;
    bookingTime?: string;
    bookingType?: string;
    checkinUrl?: string;
    conditions?: unknown;
    currency?: string;
    endTime?: string;
    modifiedTime?: string;
    partySize?: number;
    reservationId?: string;
    reservationType?: string;
    startTime?: string;
    status?: string;
    taxAmount?: number;
    totalAmount?: number;
    voidWindowEndsAt?: string;
    account?: Account;
    at?: Actor;
    broker?: Actor;
    derivedFrom?: Offer;
    event?: Event;
    location?: Place;
    order?: Order;
    passengers?: Person[];
    programMembership?: Membership;
    tickets?: Pass[];
    trips?: Trip[];
    underName?: Person;
}

export interface Result {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    community?: string;
    externalUrl?: string;
    indexedAt?: string;
    postId?: string;
    resultType?: string;
    score?: number;
    similarity?: number;
}

export interface Review {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    commentCount?: number;
    community?: string;
    externalUrl?: string;
    isVerified?: boolean;
    postType?: string;
    rating?: number;
    ratingMax?: number;
    score?: number;
    tags?: string[];
    at?: Actor;
    attachment?: File[];
    contains?: Video[];
    media?: Image[];
    postedBy?: Account;
    publish?: Community;
    replies?: Post[];
    repliesTo?: Post;
    reviews?: Product;
}

export interface Role {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    department?: string;
    endDate?: string;
    roleType?: string;
    startDate?: string;
    title?: string;
    organization?: Organization;
    person?: Person;
}

export interface Seatmap {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aircraftCode?: string;
    availableSeats?: number;
    basicEconomyLocked?: boolean;
    cabins?: unknown;
    classOfService?: string;
    departureTime?: string;
    destination?: string;
    fareBasisCode?: string;
    flightNumber?: string;
    hasExitRow?: boolean;
    hasFreeSeats?: boolean;
    hasPaidSeats?: boolean;
    origin?: string;
    tiers?: unknown;
    totalSeats?: number;
    aircraft?: Aircraft;
    at?: Actor;
    flight?: Flight;
    reservation?: Reservation;
}

export interface Shelf {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    defaultView?: string;
    iconSize?: number;
    isDefault?: boolean;
    isExclusive?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    listId?: string;
    listType?: string;
    orderingMode?: string;
    path?: string;
    privacy?: string;
    sortBy?: string;
    at?: Actor;
    backgroundImage?: Image;
    belongsTo?: Account;
    contains?: Book[];
}

export interface Simulation {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actionCount?: number;
    endedAt?: string;
    graphMode?: string;
    profile?: string;
    startedAt?: string;
    status?: string;
    task?: string;
    writeCount?: number;
    agent?: Agent;
    forkedFrom?: Simulation;
    mountedMemex?: Memex[];
    primaryMemex?: Memex;
    startedBy?: Person;
    tether?: Hardware;
}

export interface Skill {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    color?: string;
    description?: string;
    error?: string;
    skillId?: string;
    status?: string;
    privacyPolicy?: Webpage;
    termsOfService?: Webpage;
    website?: Website;
}

export interface Software {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aisle?: string;
    applicationCategory?: string;
    availability?: string;
    barcode?: string;
    calories?: number;
    categories?: string[];
    category?: string;
    codename?: string;
    currency?: string;
    customizationGroups?: unknown;
    department?: string;
    discontinued?: string;
    images?: unknown;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    price?: string;
    priceAmount?: number;
    quantity?: number;
    released?: string;
    runtimePlatform?: string;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    version?: string;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
    brand?: Brand;
    creator?: Actor[];
    inspiredBy?: Product[];
    manufacturer?: Organization;
    tagged?: Tag[];
}

export interface Sound {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    datePublished?: string;
    content?: string;
    bitDepth?: number;
    channels?: number;
    copyrightYear?: number;
    coverage?: string;
    dateCreated?: unknown;
    description?: string;
    durationMs?: number;
    encoding?: string;
    filename?: string;
    format?: string;
    kind?: string;
    language?: string;
    license?: string;
    lineCount?: number;
    mimeType?: string;
    path?: string;
    purpose?: string;
    sampleRate?: number;
    sha?: string;
    size?: number;
    tags?: string[];
    attachedTo?: Message;
    author?: Person;
    contributors?: Person[];
    copyrightHolder?: Person;
    publisher?: Organization;
    repository?: Repository;
}

export interface Source {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    address?: string;
    description?: string;
    enabled?: boolean;
    lastSynced?: string;
    scanner?: string;
    sourceId?: string;
    folder?: List;
}

export interface Spec {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    encoding?: string;
    filename?: string;
    format?: string;
    kind?: string;
    labels?: string[];
    lineCount?: number;
    mimeType?: string;
    parentId?: string;
    path?: string;
    priority?: number;
    problem?: string;
    projectId?: string;
    remoteId?: string;
    sha?: string;
    size?: number;
    startedAt?: string;
    state?: string;
    successCriteria?: string;
    target?: unknown;
    targetDate?: string;
    assignedTo?: Person;
    at?: Actor;
    attachedTo?: Message;
    blockedBy?: Task[];
    blocks?: Task[];
    children?: Task[];
    dependsOn?: Spec[];
    parent?: Task;
    project?: Project;
    repository?: Repository;
    supersedes?: Spec[];
}

export interface Tag {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    annotated?: boolean;
    color?: string;
    hash?: string;
    tagType?: string;
}

export interface Task {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    labels?: string[];
    parentId?: string;
    priority?: number;
    projectId?: string;
    remoteId?: string;
    startedAt?: string;
    state?: string;
    target?: unknown;
    targetDate?: string;
    assignedTo?: Person;
    at?: Actor;
    blockedBy?: Task[];
    blocks?: Task[];
    children?: Task[];
    parent?: Task;
    project?: Project;
    repository?: Repository;
}

export interface TaxLine {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    amount?: number;
    appliesToIndex?: number;
    code?: string;
    country?: string;
    currency?: string;
    description?: string;
    inclusive?: boolean;
    kind?: string;
    merchantImposed?: boolean;
    nature?: string;
    rate?: number;
    refundable?: boolean;
    taxableAmount?: number;
    appliesTo?: Fare;
    at?: Actor;
    imposedBy?: Actor;
    location?: Place;
    offer?: Offer;
    reservation?: Reservation;
    segment?: Leg;
}

export interface Theme {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    defaultBackgroundColor?: string;
    description?: string;
    family?: string;
    startMenu?: string;
    style?: string;
    themeId?: string;
    represents?: Product;
}

export interface ToolCall {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    durationMs?: number;
    input?: string;
    isError?: boolean;
    output?: string;
    from?: Actor;
    inMessage?: Message;
    platform?: Product;
    repliesTo?: ToolCall;
}

export interface Transaction {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    amount?: number;
    balance?: number;
    category?: string;
    currency?: string;
    details?: unknown;
    notes?: string;
    pending?: boolean;
    postingDate?: string;
    recurring?: boolean;
    type?: string;
    account?: FinancialAccount;
    at?: Actor;
}

export interface Transcript {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    contentRole?: string;
    durationMs?: number;
    language?: string;
    segmentCount?: number;
    segments?: unknown;
    sourceType?: string;
}

export interface Trip {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    arrivalTime?: string;
    bookingToken?: string;
    cabinClass?: string;
    carbonEmissions?: unknown;
    currency?: string;
    departureTime?: string;
    distance?: string;
    duration?: string;
    durationMinutes?: number;
    fare?: string;
    fareAmount?: number;
    guest?: unknown;
    isPool?: boolean;
    isReserve?: boolean;
    isScheduled?: boolean;
    isSurge?: boolean;
    marketplace?: string;
    rating?: string;
    status?: string;
    stops?: number;
    trackingUrl?: string;
    tripType?: string;
    vehicle?: unknown;
    vehicleType?: string;
    at?: Actor;
    carrier?: Organization;
    destination?: Place;
    driver?: Person;
    legs?: Leg[];
    order?: Order;
    origin?: Place;
}

export interface User {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    actorType?: string;
    osUsername?: string;
    primaryUser?: boolean;
    identifiedAs?: Person;
}

export interface Video {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    datePublished?: string;
    content?: string;
    codec?: string;
    copyrightYear?: number;
    coverage?: string;
    dateCreated?: unknown;
    description?: string;
    durationMs?: number;
    encoding?: string;
    filename?: string;
    format?: string;
    frameRate?: number;
    kind?: string;
    language?: string;
    license?: string;
    lineCount?: number;
    mimeType?: string;
    path?: string;
    resolution?: string;
    sha?: string;
    size?: number;
    tags?: string[];
    viewCount?: number;
    addTo?: Playlist;
    attachedTo?: Message;
    author?: Person;
    channel?: Channel;
    contributors?: Person[];
    copyrightHolder?: Person;
    publisher?: Organization;
    repository?: Repository;
    transcribe?: Transcript;
}

export interface Webpage {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    contentType?: string;
    error?: string;
    lastVisitUnix?: number;
    visitCount?: number;
}

export interface Website {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    anonymous?: boolean;
    claimToken?: string;
    claimUrl?: string;
    expiresAt?: string;
    status?: string;
    versionId?: string;
    domain?: Domain;
    ownedBy?: Organization;
}
