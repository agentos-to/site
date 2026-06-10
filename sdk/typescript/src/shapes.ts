// Auto-generated from shape YAML — do not edit.
// Generated from 111 shapes.
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
    allDay?: boolean;
    changedKeys?: string[];
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    duration?: number;
    endDate?: string;
    icalUid?: string;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    success?: boolean;
    timezone?: string;
    toolName?: string;
    visibility?: string;
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
    seatCapacity?: number;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    variant?: string;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
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
    iataCode?: string;
    icaoCode?: string;
    industry?: string;
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

export interface Birth {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    additionalName?: string;
    allDay?: boolean;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    familyName?: string;
    gender?: string;
    givenName?: string;
    honorificPrefix?: string;
    honorificSuffix?: string;
    icalUid?: string;
    legalName?: string;
    maidenName?: string;
    nameOrder?: string;
    nickname?: string;
    phoneticFamilyName?: string;
    phoneticGivenName?: string;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    sortAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
}

export interface Book {
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
    series?: string;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    tags?: string[];
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
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
    allDay?: boolean;
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
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    expiresAt?: string;
    feesAmount?: number;
    hasVoidWindow?: boolean;
    icalUid?: string;
    isChangeable?: boolean;
    isRefundable?: boolean;
    itineraryHash?: string;
    preparedAt?: string;
    presentedAt?: string;
    properties?: unknown;
    recurrence?: string[];
    referenceNumber?: string;
    review?: string;
    showAs?: string;
    signature?: string;
    signatureAlg?: string;
    signedBy?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    taxAmount?: number;
    timezone?: string;
    totalAmount?: number;
    visibility?: string;
    voidWindowEndsAt?: string;
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
    handle?: string;
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
    primaryColor?: string;
    tagline?: string;
    textColor?: string;
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
}

export interface Change {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    kind?: string;
    path?: string;
    phase?: string;
    status?: string;
    summary?: string;
    version?: string;
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
    capacity?: number;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    isFull?: boolean;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    spotsRemaining?: number;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
}

export interface Conversion {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allDay?: boolean;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    factor?: number;
    icalUid?: string;
    kind?: string;
    properties?: unknown;
    rate?: number;
    recurrence?: string[];
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
}

export interface CreativeWork {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    copyrightYear?: number;
    coverage?: string;
    dateCreated?: unknown;
    description?: string;
    language?: string;
    license?: string;
    tags?: string[];
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
    identifier?: string;
    itemType?: string;
    lastVerified?: string;
    obtainedAt?: string;
    refreshable?: boolean;
    source?: string;
    storeRowId?: number;
}

export interface Dimension {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    amount?: number;
    current?: number;
    dimensionless?: boolean;
    key?: string;
    label?: string;
    length?: number;
    luminous?: number;
    mass?: number;
    temperature?: number;
    time?: number;
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
    author?: string;
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
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
    identifier?: string;
    interestRate?: number;
    last4?: string;
    minimumPayment?: number;
    routingNumber?: string;
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
    allDay?: boolean;
    arrivalTime?: string;
    cabinClass?: string;
    carbonEmissions?: unknown;
    currentUrl?: string;
    dateUpdated?: string;
    departureTime?: string;
    distinctId?: string;
    duration?: string;
    durationMinutes?: number;
    endDate?: string;
    flightNumber?: string;
    icalUid?: string;
    layoverMinutes?: number;
    polyline?: string;
    properties?: unknown;
    recurrence?: string[];
    sequence?: number;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    stops?: number;
    timezone?: string;
    trace?: unknown;
    tracePointCount?: number;
    vehicleType?: string;
    visibility?: string;
}

export interface Flow {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    goal?: string;
    status?: string;
    trigger?: string;
}

export interface Font {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
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
}

export interface GitCommit {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    additions?: number;
    allDay?: boolean;
    committedAt?: string;
    currentUrl?: string;
    dateUpdated?: string;
    deletions?: number;
    distinctId?: string;
    endDate?: string;
    filesChanged?: number;
    icalUid?: string;
    message?: string;
    properties?: unknown;
    recurrence?: string[];
    sha?: string;
    shortHash?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
    allDay?: boolean;
    bodySite?: string;
    clinicalArea?: string;
    clinicalStatus?: string;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    icd10Code?: string;
    mitigation?: string;
    properties?: unknown;
    proximity?: string;
    recurrence?: string[];
    severity?: string;
    showAs?: string;
    snomedCode?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    verificationStatus?: string;
    visibility?: string;
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
    currentUrl?: string;
    cvxCode?: string;
    dateAdministered?: string;
    dateUpdated?: string;
    diseaseTarget?: string;
    distinctId?: string;
    doseNumber?: number;
    endDate?: string;
    icalUid?: string;
    lotNumber?: string;
    manufacturer?: string;
    notes?: string;
    properties?: unknown;
    recurrence?: string[];
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
    ccn?: string;
    cliaNumber?: string;
    industry?: string;
    labType?: string;
    npi?: string;
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
    allDay?: boolean;
    community?: string;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    externalUrl?: string;
    flag?: string;
    icalUid?: string;
    indexedAt?: string;
    notes?: string;
    postId?: string;
    properties?: unknown;
    recurrence?: string[];
    refHigh?: number;
    refLow?: number;
    refText?: string;
    resultType?: string;
    score?: number;
    showAs?: string;
    similarity?: number;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    value?: number;
    valueText?: string;
    visibility?: string;
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
    allDay?: boolean;
    arrangement?: string;
    currentUrl?: string;
    dateUpdated?: string;
    defaultView?: string;
    description?: string;
    distinctId?: string;
    endDate?: string;
    fasting?: boolean;
    icalUid?: string;
    iconSize?: number;
    isDefault?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    listId?: string;
    listType?: string;
    memberShape?: string;
    orderingMode?: string;
    panelCode?: string;
    path?: string;
    privacy?: string;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    sortBy?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
    bodySite?: string;
    cptCode?: string;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    findings?: string;
    followUp?: string;
    icalUid?: string;
    outcome?: string;
    performedDate?: string;
    procedureType?: string;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    snomedCode?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
    allDay?: boolean;
    category?: string;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    fasting?: boolean;
    gestationalAge?: string;
    high?: number;
    icalUid?: string;
    low?: number;
    method?: string;
    pregnancy?: string;
    properties?: unknown;
    provenance?: string;
    recurrence?: string[];
    refText?: string;
    sex?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timeOfDay?: string;
    timezone?: string;
    unit?: string;
    visibility?: string;
}

export interface Icon {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
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
}

export interface Image {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
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
}

export interface IntellectualProperty {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    category?: string;
    filingBasis?: string;
    identifier?: string;
    mark?: string;
    niceClass?: number[];
    register?: string;
    renewalPeriod?: string;
    status?: string;
    validIn?: string;
    verificationUrl?: string;
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
    allDay?: boolean;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    email?: string;
    endDate?: string;
    icalUid?: string;
    invitationType?: string;
    message?: string;
    properties?: unknown;
    recurrence?: string[];
    revokedAt?: string;
    role?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    token?: string;
    visibility?: string;
}

export interface Launch {
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
    allDay?: boolean;
    arrivalTime?: string;
    cabinClass?: string;
    carbonEmissions?: unknown;
    currentUrl?: string;
    dateUpdated?: string;
    departureTime?: string;
    distinctId?: string;
    duration?: string;
    durationMinutes?: number;
    endDate?: string;
    flightNumber?: string;
    icalUid?: string;
    layoverMinutes?: number;
    polyline?: string;
    properties?: unknown;
    recurrence?: string[];
    sequence?: number;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    trace?: unknown;
    tracePointCount?: number;
    vehicleType?: string;
    visibility?: string;
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
    arrangement?: string;
    defaultView?: string;
    iconSize?: number;
    isDefault?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    listId?: string;
    listType?: string;
    memberShape?: string;
    orderingMode?: string;
    path?: string;
    privacy?: string;
    sortBy?: string;
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
    allDay?: boolean;
    currentUrl?: string;
    dateUpdated?: string;
    digest?: string;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    properties?: unknown;
    quantization?: string;
    recurrence?: string[];
    showAs?: string;
    size?: string;
    sizeVram?: number;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
    calendarLink?: string;
    conferenceProvider?: string;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    isVirtual?: boolean;
    meetingType?: string;
    meetingUrl?: string;
    phoneDialIn?: string;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
    allDay?: boolean;
    autoRenew?: boolean;
    billingType?: string;
    currency?: string;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    guestPassQuantity?: number;
    icalUid?: string;
    price?: number;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    tier?: string;
    timezone?: string;
    useCount?: number;
    visibility?: string;
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
}

export interface Milestone {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    allDay?: boolean;
    criterion?: string;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    properties?: unknown;
    reachedAt?: string;
    recurrence?: string[];
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
}

export interface Module {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    path?: string;
    planned?: boolean;
    role?: string;
    status?: string;
    version?: string;
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
    allDay?: boolean;
    availability?: string;
    bookingToken?: string;
    currency?: string;
    currentUrl?: string;
    dateUpdated?: string;
    departureToken?: string;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    offerType?: string;
    price?: number;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
    allDay?: boolean;
    body?: string;
    currency?: string;
    currentUrl?: string;
    dateUpdated?: string;
    deliveryDate?: string;
    deliveryFee?: number;
    deliveryInstructions?: string;
    distinctId?: string;
    endDate?: string;
    eta?: string;
    fareBreakdown?: unknown;
    head?: string;
    icalUid?: string;
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
    properties?: unknown;
    recurrence?: string[];
    savings?: number;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    subtotal?: number;
    summary?: string;
    taxes?: number;
    timeline?: unknown;
    timezone?: string;
    tipAmount?: number;
    total?: string;
    totalAmount?: number;
    visibility?: string;
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
    industry?: string;
}

export interface Outcome {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    archived?: boolean;
    baseline?: string;
    current?: string;
    metric?: string;
    statement?: string;
    status?: string;
    target?: string;
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
    allDay?: boolean;
    boardingGroup?: string;
    checkinStatus?: string;
    currency?: string;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    gate?: string;
    icalUid?: string;
    isAllDayPass?: boolean;
    nameOnTicket?: string;
    price?: number;
    properties?: unknown;
    purchasedQuantity?: number;
    quantity?: number;
    recurrence?: string[];
    seatAssignment?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    terminal?: string;
    ticketClass?: string;
    ticketNumber?: string;
    timezone?: string;
    useCount?: number;
    visibility?: string;
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
    notes?: string;
}

export interface Persona {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    goals?: string[];
    headline?: string;
    painPoints?: string[];
    quote?: string;
    reachesFor?: string;
    who?: string;
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
    arrangement?: string;
    defaultView?: string;
    iconSize?: number;
    isDefault?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    listId?: string;
    listType?: string;
    memberShape?: string;
    orderingMode?: string;
    path?: string;
    privacy?: string;
    sortBy?: string;
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
}

export interface Practice {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    aliases?: string[];
    code?: string;
    codeSystem?: string;
    description?: string;
}

export interface Principle {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    domain?: string;
    rationale?: string;
    statement?: string;
    status?: string;
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
    images?: unknown;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    price?: string;
    priceAmount?: number;
    quantity?: number;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
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

export interface Qualification {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    category?: string;
    identifier?: string;
    level?: string;
    renewalPeriod?: string;
    status?: string;
    validIn?: string;
    verificationUrl?: string;
}

export interface QuantityKind {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    key?: string;
    label?: string;
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
    allDay?: boolean;
    availableActions?: string[];
    baseAmount?: number;
    bookingTime?: string;
    bookingType?: string;
    checkinUrl?: string;
    conditions?: unknown;
    currency?: string;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    endTime?: string;
    icalUid?: string;
    modifiedTime?: string;
    partySize?: number;
    properties?: unknown;
    recurrence?: string[];
    reservationId?: string;
    reservationType?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    startTime?: string;
    status?: string;
    taxAmount?: number;
    timezone?: string;
    totalAmount?: number;
    visibility?: string;
    voidWindowEndsAt?: string;
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
    allDay?: boolean;
    currentUrl?: string;
    dateUpdated?: string;
    department?: string;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    properties?: unknown;
    recurrence?: string[];
    roleType?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    title?: string;
    visibility?: string;
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
    destination?: string;
    fareBasisCode?: string;
    flightNumber?: string;
    hasExitRow?: boolean;
    hasFreeSeats?: boolean;
    hasPaidSeats?: boolean;
    origin?: string;
    tiers?: unknown;
    totalSeats?: number;
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
    arrangement?: string;
    defaultView?: string;
    iconSize?: number;
    isDefault?: boolean;
    isExclusive?: boolean;
    isPublic?: boolean;
    itemCount?: number;
    listId?: string;
    listType?: string;
    memberShape?: string;
    orderingMode?: string;
    path?: string;
    privacy?: string;
    sortBy?: string;
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
    images?: unknown;
    novaGroup?: number;
    nutritionScore?: string;
    originalPrice?: string;
    originalPriceAmount?: number;
    price?: string;
    priceAmount?: number;
    quantity?: number;
    runtimePlatform?: string;
    servingSize?: string;
    sku?: string;
    soldByWeight?: boolean;
    version?: string;
    weight?: string;
    weightUnit?: string;
    weightValue?: number;
}

export interface Sound {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
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
    allDay?: boolean;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    encoding?: string;
    endDate?: string;
    filename?: string;
    format?: string;
    icalUid?: string;
    kind?: string;
    labels?: string[];
    lineCount?: number;
    mimeType?: string;
    parentId?: string;
    path?: string;
    priority?: number;
    problem?: string;
    projectId?: string;
    properties?: unknown;
    recurrence?: string[];
    remoteId?: string;
    sha?: string;
    showAs?: string;
    size?: number;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    state?: string;
    status?: string;
    successCriteria?: string;
    target?: unknown;
    targetDate?: string;
    timezone?: string;
    visibility?: string;
}

export interface Step {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    detail?: string;
    position?: number;
    status?: string;
}

export interface Symbol {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    kind?: string;
    lang?: string;
    signature?: string;
    sourceLine?: number;
    sourcePath?: string;
    summary?: string;
    urn?: string;
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
    allDay?: boolean;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    labels?: string[];
    parentId?: string;
    priority?: number;
    projectId?: string;
    properties?: unknown;
    recurrence?: string[];
    remoteId?: string;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    state?: string;
    status?: string;
    target?: unknown;
    targetDate?: string;
    timezone?: string;
    visibility?: string;
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
    allDay?: boolean;
    amount?: number;
    balance?: number;
    category?: string;
    currency?: string;
    currentUrl?: string;
    dateUpdated?: string;
    details?: unknown;
    distinctId?: string;
    endDate?: string;
    icalUid?: string;
    notes?: string;
    pending?: boolean;
    postingDate?: string;
    properties?: unknown;
    recurrence?: string[];
    recurring?: boolean;
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    type?: string;
    visibility?: string;
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

export interface Transition {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    additionalName?: string;
    allDay?: boolean;
    currentUrl?: string;
    dateUpdated?: string;
    distinctId?: string;
    endDate?: string;
    familyName?: string;
    gender?: string;
    givenName?: string;
    honorificPrefix?: string;
    honorificSuffix?: string;
    icalUid?: string;
    legalName?: string;
    maidenName?: string;
    nameOrder?: string;
    nickname?: string;
    phoneticFamilyName?: string;
    phoneticGivenName?: string;
    properties?: unknown;
    recurrence?: string[];
    showAs?: string;
    sortAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    timezone?: string;
    visibility?: string;
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
    allDay?: boolean;
    arrivalTime?: string;
    bookingToken?: string;
    cabinClass?: string;
    carbonEmissions?: unknown;
    currency?: string;
    currentUrl?: string;
    dateUpdated?: string;
    departureTime?: string;
    distance?: string;
    distinctId?: string;
    duration?: string;
    durationMinutes?: number;
    endDate?: string;
    fare?: string;
    fareAmount?: number;
    guest?: unknown;
    icalUid?: string;
    isPool?: boolean;
    isReserve?: boolean;
    isScheduled?: boolean;
    isSurge?: boolean;
    marketplace?: string;
    properties?: unknown;
    rating?: string;
    recurrence?: string[];
    showAs?: string;
    sourceTitle?: string;
    sourceUrl?: string;
    startDate?: string;
    status?: string;
    stops?: number;
    timezone?: string;
    trackingUrl?: string;
    tripType?: string;
    vehicle?: unknown;
    vehicleType?: string;
    visibility?: string;
}

export interface Unit {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    iso4217?: string;
    iso4217Numeric?: string;
    kind?: string;
    label?: string;
    logBase?: number;
    minorExponent?: number;
    qudtUnitIri?: string;
    siDigitalFrameworkUri?: string;
    symbol?: string;
    toBaseFactor?: number;
    toBaseOffset?: number;
    ucumCode?: string;
    unCefactCommonCode?: string;
    wikidataId?: string;
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
}

export interface UserIdentity {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    active?: boolean;
    personNodeId?: string;
    userId?: string;
    volumeId?: string;
}

export interface Video {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
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
}

export interface Volume {
    id?: string;
    name?: string;
    text?: string;
    url?: string;
    image?: string;
    author?: string;
    datePublished?: string;
    content?: string;
    address?: string;
    autoMount?: boolean;
    defaultView?: string;
    freeBytes?: number;
    icon?: string;
    kind?: string;
    provider?: string;
    readOnly?: boolean;
    removable?: boolean;
    scope?: string;
    totalBytes?: number;
    volumeId?: string;
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
    status?: string;
    versionId?: string;
}

// ─── Display spec — `display:` block per shape ──────────────────────────
// The closed role vocabulary every theme renders against; the frontend's
// `resolveDisplay()` reads `SHAPE_DISPLAY[shape]` and projects a
// `DisplayModel` from a node. See core/_roadmap/p1/shape-display/plan.md.

export interface Display {
    title?: string;       // → a field (default: `name`)
    subtitle?: string;    // → a field or relation
    image?: string;       // → a field (url) or a relation → node.image
    highlights?: string[];// 0..4 fields/relations
    body?: string;        // detail-only: one long text field
    preview?: Record<string, "clip" | "full" | { max_chars: number }>;
    /** Transitive `also:` closure — the chain this shape inherits from.
     *  The resolver uses it to pick the most-specific shape on a
     *  multi-shape node (`shape[]` is alphabetical, not inheritance). */
    also: string[];
}

export const SHAPE_DISPLAY: Record<string, Display> = {
    "account": {"subtitle": "identifier", "also": []},
    "activity": {"subtitle": "action", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "actor": {"subtitle": "actorType", "also": []},
    "aircraft": {"subtitle": "model", "also": ["product"]},
    "airline": {"subtitle": "iataCode", "image": "image", "highlights": ["headquarters"], "also": ["organization", "actor"]},
    "airport": {"subtitle": "iataCode", "also": []},
    "app": {"subtitle": "name", "also": []},
    "birth": {"subtitle": "location", "highlights": ["startDate", "location"], "also": ["event"]},
    "book": {"subtitle": "written_by", "image": "image", "highlights": ["datePublished", "published_by"], "body": "description", "also": ["creative_work", "product"]},
    "booking_offer": {"subtitle": "totalAmount", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "bookmark": {"subtitle": "name", "also": []},
    "branch": {"subtitle": "commit", "also": []},
    "brand": {"subtitle": "tagline", "also": []},
    "calendar": {"subtitle": "source", "also": []},
    "change": {"subtitle": "kind", "highlights": ["status", "phase", "path"], "body": "summary", "also": []},
    "channel": {"subtitle": "subscriberCount", "also": []},
    "class": {"subtitle": "activityType", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "community": {"subtitle": "text", "also": []},
    "conversation": {"subtitle": "text", "also": []},
    "conversion": {"subtitle": "kind", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "creative_work": {"subtitle": "written_by", "image": "image", "highlights": ["datePublished", "published_by"], "body": "description", "also": []},
    "credential": {"subtitle": "source", "also": []},
    "dimension": {"subtitle": "label", "also": []},
    "dns_record": {"subtitle": "recordType", "also": []},
    "document": {"subtitle": "contentType", "highlights": ["datePublished", "author", "wordCount"], "body": "abstract", "also": ["file"]},
    "domain": {"subtitle": "registrar", "also": []},
    "email": {"subtitle": "author", "also": ["message"]},
    "episode": {"subtitle": "author", "also": []},
    "event": {"subtitle": "startDate", "highlights": ["startDate", "endDate", "location"], "also": []},
    "fare": {"subtitle": "fareFamily", "also": []},
    "file": {"subtitle": "path", "also": []},
    "financial_account": {"subtitle": "last4", "also": []},
    "flight": {"subtitle": "airline", "highlights": ["startDate", "endDate", "location"], "also": ["leg", "event"]},
    "flow": {"subtitle": "goal", "highlights": ["trigger", "status"], "also": []},
    "font": {"subtitle": "author", "image": "image", "highlights": ["datePublished", "published_by"], "body": "description", "also": ["creative_work"]},
    "git_commit": {"subtitle": "author", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "group": {"subtitle": "category", "also": []},
    "health-biomarker": {"subtitle": "category", "also": []},
    "health-condition": {"subtitle": "clinicalStatus", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "health-immunization": {"subtitle": "dateAdministered", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "health-lab": {"subtitle": "labType", "image": "image", "highlights": ["headquarters"], "also": ["organization", "actor"]},
    "health-observation": {"subtitle": "startDate", "highlights": ["startDate", "endDate", "location"], "also": ["result", "event"]},
    "health-panel": {"subtitle": "startDate", "highlights": ["startDate", "endDate", "location"], "also": ["list", "event"]},
    "health-procedure": {"subtitle": "performedDate", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "health-reference-range": {"subtitle": "refText", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "icon": {"subtitle": "purpose", "image": "image", "highlights": ["datePublished", "published_by"], "body": "description", "also": ["creative_work"]},
    "image": {"subtitle": "format", "image": "image", "highlights": ["datePublished", "published_by"], "body": "description", "also": ["creative_work", "file"]},
    "intellectual_property": {"subtitle": "category", "highlights": ["identifier", "status", "granted_by"], "also": []},
    "invitation": {"subtitle": "invitationType", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "launch": {"subtitle": "rocketId", "highlights": ["startDate", "rocketId", "launchpadId"], "also": ["event"]},
    "leg": {"subtitle": "flightNumber", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "list": {"subtitle": "name", "also": []},
    "loaded_model": {"subtitle": "size", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "mcp_session": {"subtitle": "client", "also": []},
    "meeting": {"subtitle": "location", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "membership": {"subtitle": "status", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "message": {"subtitle": "from", "also": []},
    "milestone": {"subtitle": "status", "highlights": ["status", "reachedAt"], "body": "criterion", "also": ["event"]},
    "model": {"subtitle": "name", "also": []},
    "module": {"subtitle": "role", "highlights": ["status", "path"], "also": []},
    "note": {"subtitle": "noteType", "also": []},
    "offer": {"subtitle": "price", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "order": {"subtitle": "total", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "organization": {"subtitle": "industry", "image": "image", "highlights": ["headquarters"], "also": ["actor"]},
    "outcome": {"subtitle": "status", "body": "statement", "also": []},
    "pass": {"subtitle": "status", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "payment_method": {"subtitle": "displayName", "also": []},
    "person": {"subtitle": "about", "image": "image", "highlights": ["birthdate", "gender"], "body": "notes", "also": ["actor"]},
    "persona": {"subtitle": "headline", "highlights": ["reachesFor", "quote"], "body": "who", "also": []},
    "place": {"subtitle": "featureType", "image": "image", "highlights": ["city", "country", "rating"], "body": "fullAddress", "also": []},
    "playlist": {"subtitle": "text", "also": ["list"]},
    "podcast": {"subtitle": "host", "also": []},
    "post": {"subtitle": "author", "also": []},
    "practice": {"subtitle": "parent", "also": []},
    "principle": {"subtitle": "domain", "highlights": ["statement", "status"], "body": "rationale", "also": []},
    "product": {"subtitle": "brand", "also": []},
    "project": {"subtitle": "state", "also": []},
    "protocol": {"subtitle": "name", "also": []},
    "qualification": {"subtitle": "category", "highlights": ["identifier", "validIn", "granted_by"], "also": []},
    "quantity-kind": {"subtitle": "label", "also": []},
    "quote": {"subtitle": "year", "also": []},
    "repository": {"subtitle": "language", "also": []},
    "reservation": {"subtitle": "reservationType", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "result": {"subtitle": "url", "also": []},
    "review": {"subtitle": "author", "also": ["post"]},
    "role": {"subtitle": "name", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "seatmap": {"title": "flightNumber", "also": []},
    "shelf": {"subtitle": "isExclusive", "also": ["list"]},
    "skill": {"subtitle": "description", "also": []},
    "software": {"subtitle": "applicationCategory", "highlights": ["version", "runtimePlatform"], "also": ["product"]},
    "sound": {"subtitle": "purpose", "image": "image", "highlights": ["datePublished", "published_by"], "body": "description", "also": ["creative_work", "file"]},
    "source": {"subtitle": "sourceId", "also": []},
    "spec": {"subtitle": "state", "highlights": ["startDate", "endDate", "location"], "also": ["task", "event", "file"]},
    "step": {"subtitle": "status", "highlights": ["position", "status"], "body": "detail", "also": []},
    "symbol": {"subtitle": "signature", "highlights": ["kind", "lang", "sourcePath"], "body": "summary", "also": []},
    "tag": {"title": "name", "subtitle": "tagType", "also": []},
    "task": {"subtitle": "state", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "tax_line": {"subtitle": "description", "also": []},
    "theme": {"subtitle": "family", "also": []},
    "tool_call": {"subtitle": "name", "also": []},
    "transaction": {"subtitle": "category", "highlights": ["amount", "postingDate", "currency"], "body": "notes", "also": ["event"]},
    "transcript": {"subtitle": "language", "also": []},
    "transition": {"subtitle": "startDate", "highlights": ["startDate", "givenName", "familyName", "gender"], "also": ["event"]},
    "trip": {"subtitle": "tripType", "highlights": ["startDate", "endDate", "location"], "also": ["event"]},
    "unit": {"subtitle": "symbol", "also": []},
    "user": {"subtitle": "name", "also": ["actor"]},
    "user_identity": {"subtitle": "volume_id", "highlights": ["person_node_id", "active"], "also": []},
    "video": {"subtitle": "author", "image": "image", "highlights": ["datePublished", "published_by"], "body": "description", "also": ["creative_work", "file"]},
    "volume": {"subtitle": "kind", "also": []},
    "webpage": {"subtitle": "url", "also": []},
    "website": {"subtitle": "url", "also": []},
};

// ─── Field order — YAML declaration order per shape ────────────────────
// Detail panels iterate this list and look up `node.vals[key]`. Own
// fields first, then inherited via `also:` deduped.

export const SHAPE_FIELD_ORDER: Record<string, readonly string[]> = {
    "account": ["identifier", "handle", "displayName", "display", "email", "phone", "bio", "accountType", "color", "isActive", "joinedDate", "lastActive", "lastProfileFetch", "userId", "issuer", "metadata"],
    "activity": ["action", "changedKeys", "toolName", "duration", "success", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "actor": ["actorType"],
    "aircraft": ["model", "variant", "seatCapacity", "rangeKm", "iataCode", "icaoCode", "category", "price", "priceAmount", "originalPrice", "originalPriceAmount", "currency", "categories", "availability", "images", "quantity", "weight", "weightValue", "weightUnit", "soldByWeight", "department", "aisle", "sku", "barcode", "nutritionScore", "novaGroup", "calories", "servingSize", "customizationGroups"],
    "airline": ["iataCode", "icaoCode", "callsign", "country", "alliance", "industry", "actorType"],
    "airport": ["iataCode", "icaoCode", "city", "country", "countryCode", "timezone", "elevationFt", "terminalCount"],
    "app": ["id", "name", "iconRole", "route", "defaultView", "isSystem", "handles"],
    "birth": ["givenName", "additionalName", "familyName", "honorificPrefix", "honorificSuffix", "legalName", "maidenName", "sortAs", "nameOrder", "phoneticGivenName", "phoneticFamilyName", "gender", "nickname", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "book": ["isbn", "isbn13", "pages", "genres", "series", "format", "language", "originalTitle", "places", "characters", "awardsWon", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "coverage", "tags", "category", "price", "priceAmount", "originalPrice", "originalPriceAmount", "currency", "categories", "availability", "images", "quantity", "weight", "weightValue", "weightUnit", "soldByWeight", "department", "aisle", "sku", "barcode", "nutritionScore", "novaGroup", "calories", "servingSize", "customizationGroups"],
    "booking_offer": ["cartId", "referenceNumber", "status", "preparedAt", "presentedAt", "approvedAt", "expiresAt", "currency", "baseAmount", "taxAmount", "feesAmount", "totalAmount", "itineraryHash", "signature", "signatureAlg", "signedBy", "checkoutUrl", "confirmEndpoint", "isRefundable", "isChangeable", "hasVoidWindow", "voidWindowEndsAt", "conditions", "blob", "review", "contactEmail", "contactPhone", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "bookmark": ["name", "handle"],
    "branch": ["commit", "upstream", "ahead", "behind", "isCurrent", "isRemote"],
    "brand": ["tagline", "country", "primaryColor", "textColor"],
    "calendar": ["calendarId", "color", "backgroundColor", "foregroundColor", "isPrimary", "isReadonly", "accessRole", "source", "timezone"],
    "change": ["kind", "summary", "status", "path", "phase", "version"],
    "channel": ["banner", "subscriberCount"],
    "class": ["activityType", "capacity", "spotsRemaining", "isFull", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "community": ["privacy", "memberCount", "subscriberCount", "allowCrypto"],
    "conversation": ["isGroup", "isArchived", "unreadCount", "messageCount", "accountEmail", "historyId", "source", "cwd", "gitBranch"],
    "conversion": ["kind", "factor", "rate", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "creative_work": ["name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags"],
    "credential": ["domain", "identifier", "itemType", "source", "obtainedAt", "lastVerified", "refreshable", "storeRowId"],
    "dimension": ["key", "label", "length", "mass", "time", "current", "temperature", "amount", "luminous", "dimensionless"],
    "dns_record": ["domain", "recordName", "recordType", "type", "ttl", "priority", "recordId", "values"],
    "document": ["contentType", "language", "wordCount", "abstract", "tableOfContents", "filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"],
    "domain": ["status", "registrar", "autoRenew", "nameservers"],
    "email": ["subject", "messageId", "inReplyTo", "isUnread", "isStarred", "isDraft", "isSent", "isTrash", "isSpam", "hasAttachments", "draftId", "conversationId", "accountEmail", "sizeEstimate", "references", "replyTo", "deliveredTo", "attachments", "toRaw", "ccRaw", "bccRaw", "unsubscribe", "unsubscribeOneClick", "manageSubscription", "listId", "isAutomated", "precedence", "mailer", "returnPath", "authResults", "bodyHtml", "isOutgoing"],
    "episode": ["durationMs", "episodeNumber", "seasonNumber"],
    "event": ["startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "fare": ["identifier", "bookingCode", "productType", "fareFamily", "class", "basePrice", "currency", "passengerType", "milesEarned", "pointsEarned", "components", "refundable", "changeable", "restrictions", "conditions"],
    "file": ["filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"],
    "financial_account": ["identifier", "accountId", "accountNumber", "routingNumber", "last4", "currency", "accountType", "balance", "available", "creditLimit", "minimumPayment", "cardType", "interestRate"],
    "flight": ["flightNumber", "durationMinutes", "cabinClass", "stops", "carbonEmissions", "sequence", "departureTime", "arrivalTime", "duration", "vehicleType", "layoverMinutes", "trace", "tracePointCount", "polyline", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "flow": ["goal", "trigger", "status"],
    "font": ["family", "genericFamily", "postscriptName", "weights", "styles", "formats", "scripts", "glyphCount", "designerUrl", "vendorUrl", "licenseInfoUrl", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags"],
    "git_commit": ["sha", "shortHash", "message", "additions", "deletions", "filesChanged", "committedAt", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "group": ["memberCount", "category"],
    "health-biomarker": ["measure", "category", "loincCode", "analyteType", "description"],
    "health-condition": ["clinicalStatus", "verificationStatus", "proximity", "bodySite", "severity", "snomedCode", "icd10Code", "clinicalArea", "mitigation", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "health-immunization": ["dateAdministered", "cvxCode", "manufacturer", "lotNumber", "doseNumber", "seriesDoses", "site", "route", "diseaseTarget", "notes", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "health-lab": ["cliaNumber", "npi", "ccn", "labType", "accreditation", "industry", "actorType"],
    "health-observation": ["value", "valueText", "refLow", "refHigh", "refText", "flag", "status", "notes", "indexedAt", "resultType", "externalUrl", "postId", "score", "similarity", "community", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "health-panel": ["panelCode", "fasting", "description", "id", "listId", "listType", "ordering_mode", "member_shape", "privacy", "isDefault", "isPublic", "itemCount", "arrangement", "default_view", "icon_size", "sort_by", "path", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "health-procedure": ["performedDate", "procedureType", "bodySite", "outcome", "status", "cptCode", "snomedCode", "findings", "followUp", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "health-reference-range": ["low", "high", "unit", "refText", "category", "provenance", "method", "ageLow", "ageHigh", "sex", "pregnancy", "gestationalAge", "fasting", "timeOfDay", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "icon": ["dimension", "format", "url", "component", "purpose", "style", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "language", "coverage", "tags"],
    "image": ["width", "height", "format", "altText", "appName", "windowId", "displayId", "displayIndex", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags", "filename", "mimeType", "size", "path", "encoding", "lineCount", "kind", "sha"],
    "intellectual_property": ["category", "mark", "identifier", "register", "status", "filingBasis", "niceClass", "validIn", "renewalPeriod", "verificationUrl"],
    "invitation": ["invitationType", "email", "role", "status", "token", "acceptedAt", "revokedAt", "message", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "launch": ["flightNumber", "rocketId", "launchpadId", "crewIds", "reusedBoosters", "landingOutcomes", "articleUrl", "webcastUrl", "wikipediaUrl", "patchImage", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "leg": ["sequence", "departureTime", "arrivalTime", "duration", "durationMinutes", "flightNumber", "cabinClass", "vehicleType", "layoverMinutes", "carbonEmissions", "trace", "tracePointCount", "polyline", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "list": ["id", "listId", "listType", "ordering_mode", "member_shape", "privacy", "isDefault", "isPublic", "itemCount", "arrangement", "default_view", "icon_size", "sort_by", "path"],
    "loaded_model": ["size", "quantization", "vramUsage", "sizeVram", "digest", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "mcp_session": ["client", "projectId", "gitBranch", "sessionType", "startedAt", "endedAt", "messageCount", "tokenCount"],
    "meeting": ["calendarLink", "isVirtual", "meetingUrl", "conferenceProvider", "phoneDialIn", "meetingType", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "membership": ["status", "tier", "autoRenew", "price", "currency", "billingType", "useCount", "guestPassQuantity", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "message": ["isOutgoing", "isStarred", "conversationId"],
    "milestone": ["reachedAt", "criterion", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "model": ["contextLength", "contextWindow", "maxOutput", "pricingInput", "pricingOutput", "modality", "modelType", "quantization", "quantizationLevel", "size", "parameterSize", "format", "family", "digest"],
    "module": ["name", "role", "path", "version", "status", "planned"],
    "note": ["noteType", "isPinned"],
    "offer": ["price", "currency", "offerType", "availability", "bookingToken", "departureToken", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "order": ["orderId", "orderDate", "total", "totalAmount", "originalTotal", "originalTotalAmount", "savings", "currency", "status", "deliveryDate", "eta", "subtotal", "tipAmount", "deliveryFee", "taxes", "summary", "fareBreakdown", "deliveryInstructions", "interactionType", "orderUuid", "body", "head", "messages", "timeline", "itemStates", "latestArrival", "progress", "progressTotal", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "organization": ["industry", "actorType"],
    "outcome": ["statement", "status", "archived", "metric", "baseline", "current", "target"],
    "pass": ["status", "quantity", "purchasedQuantity", "useCount", "isAllDayPass", "price", "currency", "ticketNumber", "nameOnTicket", "seatAssignment", "boardingGroup", "ticketClass", "gate", "terminal", "checkinStatus", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "payment_method": ["identifier", "type", "subtype", "brand", "displayName", "customDescription", "holderName", "last4", "binRange", "expMonth", "expYear", "expirationDate", "currency", "balance", "fingerprint", "isDefault", "isPrimary", "isExpired", "isSelected", "status", "providerTokens", "metadata"],
    "person": ["url", "notes", "about", "actorType"],
    "persona": ["headline", "who", "goals", "painPoints", "reachesFor", "quote"],
    "place": ["fullAddress", "placeFormatted", "streetNumber", "street", "neighborhood", "locality", "city", "district", "region", "postalCode", "country", "countryCode", "latitude", "longitude", "accuracy", "featureType", "categories", "phone", "website", "hours", "businessStatus", "rating", "reviewCount", "priceLevel", "timezone", "eta", "isOrderable", "closedMessage", "productCount", "mapboxId", "wikidataId", "googlePlaceId"],
    "playlist": ["id", "listId", "listType", "ordering_mode", "member_shape", "privacy", "isDefault", "isPublic", "itemCount", "arrangement", "default_view", "icon_size", "sort_by", "path"],
    "podcast": ["feedUrl"],
    "post": ["externalUrl", "postType", "score", "commentCount", "community"],
    "practice": ["description", "code", "codeSystem", "aliases"],
    "principle": ["name", "statement", "rationale", "domain", "status"],
    "product": ["category", "price", "priceAmount", "originalPrice", "originalPriceAmount", "currency", "categories", "availability", "images", "quantity", "weight", "weightValue", "weightUnit", "soldByWeight", "department", "aisle", "sku", "barcode", "nutritionScore", "novaGroup", "calories", "servingSize", "customizationGroups"],
    "project": ["state", "color", "parentId"],
    "protocol": ["name", "homepage", "rfc", "wikidataId"],
    "qualification": ["category", "identifier", "status", "renewalPeriod", "level", "validIn", "verificationUrl"],
    "quantity-kind": ["key", "label"],
    "quote": ["context", "year"],
    "repository": ["stars", "forks", "language", "topics", "openIssues", "isArchived", "isPrivate", "defaultBranch", "license", "size"],
    "reservation": ["reservationType", "reservationId", "status", "bookingType", "bookingTime", "modifiedTime", "startTime", "endTime", "partySize", "totalAmount", "baseAmount", "taxAmount", "currency", "checkinUrl", "conditions", "voidWindowEndsAt", "availableActions", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "result": ["indexedAt", "resultType", "externalUrl", "postId", "score", "similarity", "community"],
    "review": ["rating", "ratingMax", "tags", "isVerified", "externalUrl", "postType", "score", "commentCount", "community"],
    "role": ["title", "department", "roleType", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "seatmap": ["flightNumber", "origin", "destination", "fareBasisCode", "classOfService", "aircraftCode", "totalSeats", "availableSeats", "cabins", "tiers", "hasExitRow", "hasFreeSeats", "hasPaidSeats", "basicEconomyLocked"],
    "shelf": ["isExclusive", "id", "listId", "listType", "ordering_mode", "member_shape", "privacy", "isDefault", "isPublic", "itemCount", "arrangement", "default_view", "icon_size", "sort_by", "path"],
    "skill": ["skillId", "description", "color", "status", "error"],
    "software": ["version", "applicationCategory", "runtimePlatform", "codename", "category", "price", "priceAmount", "originalPrice", "originalPriceAmount", "currency", "categories", "availability", "images", "quantity", "weight", "weightValue", "weightUnit", "soldByWeight", "department", "aisle", "sku", "barcode", "nutritionScore", "novaGroup", "calories", "servingSize", "customizationGroups"],
    "sound": ["durationMs", "channels", "sampleRate", "bitDepth", "purpose", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags", "filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"],
    "source": ["sourceId", "address", "scanner", "enabled", "description", "lastSynced"],
    "spec": ["problem", "successCriteria", "remoteId", "priority", "state", "labels", "targetDate", "target", "parentId", "projectId", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties", "filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"],
    "step": ["position", "detail", "status"],
    "symbol": ["urn", "kind", "lang", "signature", "summary", "sourcePath", "sourceLine"],
    "tag": ["color", "tagType", "annotated", "hash"],
    "task": ["remoteId", "priority", "state", "labels", "targetDate", "target", "parentId", "projectId", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "tax_line": ["code", "description", "amount", "currency", "kind", "nature", "country", "appliesToIndex", "refundable", "merchantImposed", "rate", "taxableAmount", "inclusive"],
    "theme": ["themeId", "family", "description", "style", "startMenu", "defaultBackgroundColor"],
    "tool_call": ["name", "input", "output", "isError", "durationMs"],
    "transaction": ["amount", "currency", "balance", "category", "postingDate", "pending", "recurring", "notes", "type", "details", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "transcript": ["language", "sourceType", "contentRole", "durationMs", "segmentCount", "segments"],
    "transition": ["givenName", "additionalName", "familyName", "honorificPrefix", "honorificSuffix", "legalName", "maidenName", "sortAs", "nameOrder", "phoneticGivenName", "phoneticFamilyName", "gender", "nickname", "startDate", "endDate", "timezone", "allDay", "recurrence", "status", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "trip": ["tripType", "status", "departureTime", "arrivalTime", "duration", "durationMinutes", "distance", "vehicleType", "cabinClass", "fare", "fareAmount", "currency", "rating", "trackingUrl", "isSurge", "isScheduled", "stops", "bookingToken", "carbonEmissions", "isPool", "isReserve", "guest", "marketplace", "vehicle", "startDate", "endDate", "timezone", "allDay", "recurrence", "visibility", "showAs", "dateUpdated", "sourceUrl", "sourceTitle", "icalUid", "distinctId", "currentUrl", "properties"],
    "unit": ["ucumCode", "symbol", "label", "kind", "siDigitalFrameworkUri", "unCefactCommonCode", "qudtUnitIri", "wikidataId", "toBaseFactor", "toBaseOffset", "iso4217", "iso4217Numeric", "minorExponent", "logBase"],
    "user": ["osUsername", "primaryUser", "actorType"],
    "user_identity": ["user_id", "volume_id", "person_node_id", "active"],
    "video": ["durationMs", "resolution", "frameRate", "codec", "viewCount", "name", "description", "license", "copyrightYear", "datePublished", "dateCreated", "url", "language", "coverage", "tags", "filename", "mimeType", "size", "path", "format", "encoding", "lineCount", "kind", "sha"],
    "volume": ["volume_id", "kind", "address", "provider", "auto_mount", "readOnly", "removable", "totalBytes", "freeBytes", "scope", "icon", "default_view"],
    "webpage": ["visitCount", "lastVisitUnix", "contentType", "error"],
    "website": ["status", "versionId", "anonymous", "claimToken", "claimUrl"],
};

// ─── Event types — shapes whose `also:` chain includes `event` ──────────
// Derived from the shape graph — the shape IS the type.

export const EVENT_TYPES: readonly string[] = [
    "activity",
    "birth",
    "booking_offer",
    "class",
    "conversion",
    "event",
    "flight",
    "git_commit",
    "health-condition",
    "health-immunization",
    "health-observation",
    "health-panel",
    "health-procedure",
    "health-reference-range",
    "invitation",
    "launch",
    "leg",
    "loaded_model",
    "meeting",
    "membership",
    "milestone",
    "offer",
    "order",
    "pass",
    "reservation",
    "role",
    "spec",
    "task",
    "transaction",
    "transition",
    "trip",
] as const;

// ─── Derived bindings per shape — read-side resolver input ──────────────
// Binding grammar: {find, where, where_link, is, get} | {latest: [...]} | dotted string.

export const SHAPE_DERIVED: Record<string, Record<string, unknown>> = {
    "person": {"birthdate": {"find": "born_in", "is": "birth", "get": "startDate"}, "current_residence": {"find": "lived_at", "where_link": {"to": null}, "get": "name"}, "current_role": {"find": "worked_at", "where_link": {"to": null}, "get": "title"}, "givenName": {"latest": [{"find": "born_in", "is": "birth", "get": "givenName"}, {"find": "changed", "is": "transition", "get": "givenName"}]}, "additionalName": {"latest": [{"find": "born_in", "is": "birth", "get": "additionalName"}, {"find": "changed", "is": "transition", "get": "additionalName"}]}, "familyName": {"latest": [{"find": "born_in", "is": "birth", "get": "familyName"}, {"find": "changed", "is": "transition", "get": "familyName"}]}, "honorificPrefix": {"latest": [{"find": "born_in", "is": "birth", "get": "honorificPrefix"}, {"find": "changed", "is": "transition", "get": "honorificPrefix"}]}, "honorificSuffix": {"latest": [{"find": "born_in", "is": "birth", "get": "honorificSuffix"}, {"find": "changed", "is": "transition", "get": "honorificSuffix"}]}, "legalName": {"latest": [{"find": "born_in", "is": "birth", "get": "legalName"}, {"find": "changed", "is": "transition", "get": "legalName"}]}, "maidenName": {"latest": [{"find": "born_in", "is": "birth", "get": "maidenName"}, {"find": "changed", "is": "transition", "get": "maidenName"}]}, "sortAs": {"latest": [{"find": "born_in", "is": "birth", "get": "sortAs"}, {"find": "changed", "is": "transition", "get": "sortAs"}]}, "nameOrder": {"latest": [{"find": "born_in", "is": "birth", "get": "nameOrder"}, {"find": "changed", "is": "transition", "get": "nameOrder"}]}, "phoneticGivenName": {"latest": [{"find": "born_in", "is": "birth", "get": "phoneticGivenName"}, {"find": "changed", "is": "transition", "get": "phoneticGivenName"}]}, "phoneticFamilyName": {"latest": [{"find": "born_in", "is": "birth", "get": "phoneticFamilyName"}, {"find": "changed", "is": "transition", "get": "phoneticFamilyName"}]}, "gender": {"latest": [{"find": "born_in", "is": "birth", "get": "gender"}, {"find": "changed", "is": "transition", "get": "gender"}]}, "nickname": {"latest": [{"find": "born_in", "is": "birth", "get": "nickname"}, {"find": "changed", "is": "transition", "get": "nickname"}]}},
};

// ─── Shortcuts per shape — write-side flat-create expansion table ───────
// Each entry: flat_key -> {writes: <link>[is=<shape>].<field>}

export const SHAPE_SHORTCUTS: Record<string, Record<string, unknown>> = {
    "person": {"birthdate": {"writes": "born_in[is=birth].startDate"}, "givenName": {"writes": "born_in[is=birth].givenName"}, "additionalName": {"writes": "born_in[is=birth].additionalName"}, "familyName": {"writes": "born_in[is=birth].familyName"}, "honorificPrefix": {"writes": "born_in[is=birth].honorificPrefix"}, "honorificSuffix": {"writes": "born_in[is=birth].honorificSuffix"}, "legalName": {"writes": "born_in[is=birth].legalName"}, "maidenName": {"writes": "born_in[is=birth].maidenName"}, "sortAs": {"writes": "born_in[is=birth].sortAs"}, "nameOrder": {"writes": "born_in[is=birth].nameOrder"}, "phoneticGivenName": {"writes": "born_in[is=birth].phoneticGivenName"}, "phoneticFamilyName": {"writes": "born_in[is=birth].phoneticFamilyName"}, "gender": {"writes": "born_in[is=birth].gender"}, "nickname": {"writes": "born_in[is=birth].nickname"}},
};
